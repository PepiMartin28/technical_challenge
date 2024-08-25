from fastapi import APIRouter, HTTPException, status

from app.core.typesense_client import client
from app.schemas.search import SearchParameterSchema
from app.utils.search_functions import build_search_parameters, map_facet_counts, map_hits

search_routes = APIRouter()

@search_routes.post("/", tags=["search"], status_code=status.HTTP_200_OK)
async def search_tracks(parameters: SearchParameterSchema):
    search_parameters = build_search_parameters(parameters)
    
    try:
        result = client.collections['tracks'].documents.search(search_parameters)
        
        sort_options = map_facet_counts(result["facet_counts"])
        
        hits = map_hits(result["hits"])
        
        return {
            "response": {
                "sort_options": sort_options,
                "hits": hits,
                "page": parameters.page_num,
                "items_per_page": parameters.items_per_page
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")

    