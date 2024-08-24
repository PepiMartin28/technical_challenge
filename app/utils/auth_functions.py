from fastapi import HTTPException, Header

from app.core.supabase_client import supabase

async def is_user_authenticated(authorization = Header(...)):    
    token = authorization.split(" ")[1]
    authenticated = supabase.auth.get_user(token)
    if authenticated is None:
        raise HTTPException(status_code=401, detail="Invalid access token.")
    return authenticated