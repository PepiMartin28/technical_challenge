from fastapi import APIRouter, HTTPException, Query

from app.db.connection import session
from app.db.models.track import Track
from app.schemas.track import TrackSchema
from app.schemas.pagination import PaginationSchema

track_routes = APIRouter()

@track_routes.post("/", tags=["tracks"], response_model=TrackSchema)
def post_track(track: TrackSchema):
    
    # try:
    #     new_track = Track(**track.model_dump())
    #     session.add(new_track)
    #     session.commit()
        
    #     return {'message': 'The track has been created succesfully'}
    # except Exception as e:
    #     session.rollback()
    #     raise HTTPException(status_code=500, detail="An error occurred, please try later")
    return track

@track_routes.get("/", tags=["tracks"], response_model=PaginationSchema)
def list_tracks(
    page_num: int = Query(1, ge=1),
    items_per_page: int = Query(200, ge=1, le=1000)
):
    try:
        offset = (page_num - 1) * items_per_page
        
        total_tracks = session.query(Track).count()

        tracks = session.query(Track).order_by(Track.id).offset(offset).limit(items_per_page).all()
        
        if not tracks:
            raise HTTPException(status_code=404, detail="There isn't tracks in the database.")
        
        track_schemas = [TrackSchema.model_validate(track) for track in tracks]
        
        total_pages = (total_tracks + items_per_page - 1) // items_per_page 

        response = PaginationSchema(
            total_pages= total_pages,
            page = page_num,
            items_per_page = items_per_page,
            total_items = total_tracks,
            data = track_schemas
        )
        
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred, please try later")


@track_routes.get("/{id}", tags=["tracks"], response_model=TrackSchema)
def get_track(id: int):
    try:
        result = session.query(Track).filter_by(id = id).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Track not found")
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    
@track_routes.put("/{id}", tags=["tracks"], response_model=TrackSchema)
def update_track(id: int, track:TrackSchema):
    try:
        track_update = session.query(Track).filter_by(id = id).first()

        if track_update is None:
            raise HTTPException(status_code=404, detail="Track not found")
        
        track_update.title = track.title
        track_update.length_s = track.length_s
        
        session.commit()
        
        return {'message': 'The track has been updated succesfully'}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    
@track_routes.put("/{id}", tags=["tracks"], response_model=TrackSchema)
def delete_track(id: int):
    try:
        track_delete = session.query(Track).filter_by(id = id).first()

        if track_delete is None:
            raise HTTPException(status_code=404, detail="Track not found")
        
        track_delete.active = False
        
        session.commit()
        
        return {'message': 'The track has been deleted succesfully'}
    
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred, please try later")
    

    
