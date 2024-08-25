from fastapi import FastAPI

from app.api.endpoints.track_routes import track_routes
from app.api.endpoints.release_routes import realease_routes
from app.api.endpoints.auth_routes import auth_routes
from app.api.endpoints.search_routes import search_routes 


app = FastAPI(title='Technical Challenge')
    
app.include_router(track_routes, prefix="/api/v1/track")
app.include_router(realease_routes, prefix="/api/v1/release")
app.include_router(auth_routes, prefix="/api/v1/auth")
app.include_router(search_routes, prefix="/api/v1/search")