from fastapi import APIRouter, HTTPException, Query, Depends

from app.db.connection import session
from app.db.models.release import Release
from app.db.models.release_type import Release_Type
from app.schemas.release import ReleaseSchema, ReleaseCreateSchema, ReleaseUpdateSchema
from app.schemas.pagination import PaginationSchema
from app.utils.general_functions import get_item_by_id, update_fields
from app.utils.auth_functions import is_user_authenticated

realease_routes = APIRouter()

@realease_routes.post("/", tags=["release"])
async def post_release(release: ReleaseCreateSchema, authenticated = Depends(is_user_authenticated)):
    try:
        get_item_by_id(release.release_type_id, session, Release_Type)
    except:
        raise HTTPException(status_code=404, detail="There is no release type with this id.")
    
    try:
        new_release = Release(**release.model_dump())
        session.add(new_release)
        session.commit()
        session.refresh(new_release)
        return {'message': 'The release has been created succesfully.', 'data':new_release}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")

@realease_routes.get("/", tags=["release"], response_model=PaginationSchema)
async def list_releases(
    page_num: int = Query(1, ge=1),
    items_per_page: int = Query(100, ge=1, le=1000)
):
    try:
        offset = (page_num - 1) * items_per_page
        
        total_releases = session.query(Release).count()

        releases = session.query(Release).order_by(Release.id).offset(offset).limit(items_per_page).all()
        
        if not releases:
            raise HTTPException(status_code=404, detail="There isn't releases in the database.")
        
        release_schemas = [ReleaseSchema.model_validate(release) for release in releases]
        
        total_pages = (total_releases + items_per_page - 1) // items_per_page 

        return PaginationSchema(
            total_pages= total_pages,
            page = page_num,
            items_per_page = items_per_page,
            total_items = total_releases,
            data = release_schemas
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")


@realease_routes.get("/{id}", tags=["release"], response_model=ReleaseSchema)
async def get_release(id: int, authenticated = Depends(is_user_authenticated)):
    try:
        release = get_item_by_id(id, session, Release)
        
        return release
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
@realease_routes.put("/{id}", tags=["release"])
async def update_release(id: int, release:ReleaseUpdateSchema, authenticated = Depends(is_user_authenticated)):
    try:
        get_item_by_id(release.release_type_id, session, Release_Type)
    except:
        raise HTTPException(status_code=404, detail="There is no release type with this id.")
    
    try:
        release_update = get_item_by_id(id, session, Release)
        
        update_fields(release_update, release.model_dump(exclude_unset=True))
        
        session.commit()
        session.refresh(release_update)
        
        return {'message': 'The track has been updated succesfully.', 'data': release_update}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
@realease_routes.delete("/{id}", tags=["release"])
async def delete_release(id: int, authenticated = Depends(is_user_authenticated)):
    try:
        release_delete = get_item_by_id(id, session, Release)
        
        release_delete.active = False
        
        session.commit()
        
        return {'message': 'The release has been deleted succesfully.'}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    

    
