from fastapi import HTTPException
from sqlalchemy import select

from app.core.typesense_client import client
from app.db.models.artist import Artist
from app.db.models.country import Country
from app.db.models.release import Release
from app.db.models.release_country import Release_Country
from app.db.models.release_type import Release_Type
from app.db.models.track import Track
from app.db.models.track_artist import Track_Artist

def add_track_typesense(id, session):
    try:
        query = (
            session.query(
                Track.id,
                Track.name.label("title"),
                Artist.name.label("artist"),
                Release.name.label("album"),
                Release_Type.name.label("release_type"),
                Release_Country.release_year,
                Country.name.label("release_country"),
            )
            .join(Track_Artist, Track.id == Track_Artist.track_id)
            .join(Artist, Track_Artist.artist_id == Artist.id)
            .join(Release, Track.release_id == Release.id)
            .outerjoin(Release_Type, Release.release_type_id == Release_Type.id)
            .join(Release_Country, Release.id == Release_Country.release_id)
            .outerjoin(Country, Release_Country.country_id == Country.id)
            .filter(Track.id == id)
        )

        result = session.execute(query).fetchall()
        
        artists = [row.artist for row in result]
        
        document = {
            "title": result[0].title,
            "album": result[0].album,
            "artist": artists,
            "release_type": result[0].release_type,
            "release_country": result[0].release_country,
            "release_year": result[0].release_year,
            "release_decade": f"{str(result[0].release_year)[:3]}0s"
        }
        
        client.collections['tracks'].documents.create(document)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
