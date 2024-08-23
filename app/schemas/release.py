from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime

class ReleaseSchema(BaseModel):
    id: Optional[int] = None
    name: str
    active: Optional[bool] = None
    release_type: Union[int, str]
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes=True
        
