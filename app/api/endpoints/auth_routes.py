from fastapi import APIRouter, HTTPException

from app.core.supabase_client import supabase
from app.schemas.auth import AuthSchema

auth_routes = APIRouter()

@auth_routes.post("/signup", tags=["auth"])
async def sign_up(user: AuthSchema):
    try:
        user = supabase.auth.sign_up(user.model_dump())
        return {"message": "User signed up successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    
@auth_routes.post("/signin", tags=["auth"])
async def sign_up(user: AuthSchema):
    try:
        user = supabase.auth.sign_in_with_password(user.model_dump())
        return {"message": "User signed up successfully", "token": user.session.access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred, please try later.")
    