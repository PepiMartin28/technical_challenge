from app.schemas.search import FacetListSchema, FacetSchema, HitSchema

def build_search_parameters(parameters):
    query = {
        'q': parameters.query,
        'query_by': parameters.query_items,
        'facet_by': 'artist, release_decade, release_type, release_country',
        'page': parameters.page_num,
        'per_page': parameters.items_per_page
    }

    if parameters.filter_items:
        filters = []
        for filter_item in parameters.filter_items:
            filter_str = f"{filter_item.field}:[{','.join(filter_item.value)}]"
            filters.append(filter_str)
        query['filter_by'] = " && ".join(filters)
    
    if parameters.sort_direction:
        query['sort_by'] = f"release_year:{parameters.sort_direction}"
    
    return query

def map_facet_counts(facet_counts):
    return [
        FacetListSchema(
            field=facet["field_name"], 
            counts=[
                FacetSchema(value=count["value"], qty=count["count"]) 
                for count in facet["counts"]
            ]
        ) 
        for facet in facet_counts
    ]

def map_hits(hits):
    return [
        HitSchema(
            album=hit["document"]["album"], 
            title=hit["document"]["title"], 
            artist=hit["document"]["artist"], 
            release_year=hit["document"]["release_year"]
        ) 
        for hit in hits
    ]