from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import label

from app.db.connection import session
from app.db.models.release import Release
from app.db.models.release_type import Release_Type
from app.schemas.release import ReleaseSchema
from app.schemas.pagination import PaginationSchema

realease_routes = APIRouter()

@realease_routes.post("/", tags=["release"], response_model=ReleaseSchema)
def post_release(releaese: ReleaseSchema):
    
    # try:
    #     new_releaese = Release(**releaese.model_dump())
    #     session.add(new_releaese)
    #     session.commit()
        
    #     return {'message': 'The release has been created succesfully'}
    # except Exception as e:
    #     session.rollback()
    #     raise HTTPException(status_code=500, detail="An error occurred, please try later")
    return releaese

@realease_routes.get("/", tags=["release"], response_model=PaginationSchema)
def list_releases(
    page_num: int = Query(1, ge=1),
    items_per_page: int = Query(100, ge=1, le=1000)
):
    try:
        offset = (page_num - 1) * items_per_page
        
        total_releaeses = session.query(Release).count()
        
        query = (
            session.query(
                Release.id,
                Release.name,
                Release.active,
                Release.created_at,
                label('release_type', Release_Type.name)
            )
            .join(Release_Type, Release.release_type_id == Release_Type.id)
            .order_by(Release.id)
            .offset(offset)
            .limit(items_per_page)
        )

        releaeses = query.all()
        
        if not releaeses:
            raise HTTPException(status_code=404, detail="There isn't releases in the database.")
        
        release_schemas = [ReleaseSchema.model_validate(releaese) for releaese in releaeses]
        
        total_pages = (total_releaeses + items_per_page - 1) // items_per_page 

        response = PaginationSchema(
            total_pages= total_pages,
            page = page_num,
            items_per_page = items_per_page,
            total_items = total_releaeses,
            data = release_schemas
        )
        
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred, please try later")


@realease_routes.get("/{id}", tags=["release"], response_model=ReleaseSchema)
def get_release(id: int):
    try:
        result = session.query(Release).filter_by(id = id).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Release not found")
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    
@realease_routes.put("/{id}", tags=["release"], response_model=ReleaseSchema)
def update_release(id: int, track:ReleaseSchema):
    try:
        release_update = session.query(Release).filter_by(id = id).first()

        if release_update is None:
            raise HTTPException(status_code=404, detail="Track not found")
        
        release_update.title = track.title
        
        session.commit()
        
        return {'message': 'The track has been updated succesfully'}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    
@realease_routes.put("/{id}", tags=["release"], response_model=ReleaseSchema)
def delete_release(id: int):
    try:
        release_delete = session.query(Release).filter_by(id = id).first()

        if release_delete is None:
            raise HTTPException(status_code=404, detail="Release not found")
        
        release_delete.active = False
        
        session.commit()
        
        return {'message': 'The release has been deleted succesfully'}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    

    
