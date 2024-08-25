from fastapi import APIRouter, HTTPException, Query, Depends, status

from app.db.connection import session
from app.db.models.track import Track
from app.db.models.release import Release
from app.schemas.track import TrackSchema, TrackCreateSchema, TrackUpdateSchema
from app.schemas.pagination import PaginationSchema
from app.utils.general_functions import get_item_by_id, update_fields
from app.utils.auth_functions import is_user_authenticated

track_routes = APIRouter()

@track_routes.post("/", tags=["tracks"], status_code=status.HTTP_201_CREATED)
async def post_track(track: TrackCreateSchema, authenticated = Depends(is_user_authenticated)):
    try:
        get_item_by_id(track.release_id, session, Release)
    except:
        raise HTTPException(status_code=404, detail="There is no release with this id.")
    
    try:
        new_track = Track(**track.model_dump())
        session.add(new_track)
        session.commit()
        session.refresh(new_track)
        return {'message': 'The track has been created succesfully.','data': new_track}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")

@track_routes.get("/", tags=["tracks"], response_model=PaginationSchema, status_code=status.HTTP_200_OK)
async def list_tracks(
    page_num: int = Query(1, ge=1),
    items_per_page: int = Query(200, ge=1, le=1000)
):
    try:
        offset = (page_num - 1) * items_per_page
        total_tracks = session.query(Track).count()
        tracks = session.query(Track).order_by(Track.id).offset(offset).limit(items_per_page).all()
        
        if not tracks:
            raise HTTPException(status_code=404, detail="There are no tracks in the database.")
        
        track_schemas = [TrackSchema.model_validate(track) for track in tracks]
        total_pages = (total_tracks + items_per_page - 1) // items_per_page 

        return PaginationSchema(
            total_pages=total_pages,
            page=page_num,
            items_per_page=items_per_page,
            total_items=total_tracks,
            data=track_schemas
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")


@track_routes.get("/{id}", tags=["tracks"], response_model=TrackSchema, status_code=status.HTTP_200_OK)
async def get_track(id: int, authenticated = Depends(is_user_authenticated)):
    try:
        track = get_item_by_id(id, session, Track)
        
        return track
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
@track_routes.put("/{id}", tags=["tracks"], status_code=status.HTTP_200_OK)
async def update_track(id: int, track:TrackUpdateSchema, authenticated = Depends(is_user_authenticated)):
    try:
        track_update = get_item_by_id(id, session, Track)
        
        update_fields(track_update, track.model_dump(exclude_unset=True))
        
        session.commit()
        session.refresh(track_update)
        
        return {'message': 'The track has been updated succesfully.', 'data':track_update}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
@track_routes.delete("/{id}", tags=["tracks"], status_code=status.HTTP_200_OK)
async def delete_track(id: int, authenticated = Depends(is_user_authenticated)):
    try:
        track_delete = get_item_by_id(id, session, Track)
        
        track_delete.active = False
        
        session.commit()
        
        return {'message': 'The track has been deleted succesfully.'}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
