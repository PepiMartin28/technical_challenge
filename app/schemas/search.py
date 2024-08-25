from pydantic import BaseModel
from typing import List, Any, Optional

class FacetListSchema(BaseModel):
    field: str
    counts: List[Any]
    
class FacetSchema(BaseModel):
    value: str
    qty: int

class HitSchema(BaseModel):
    title: str
    album: str
    artist: List[str]
    release_year: int
    
class FilterSchema(BaseModel):
    field: str
    value: List[str]
    
class SearchParameterSchema(BaseModel):
    query: str
    query_items: str = 'title'
    sort_direction: Optional[str] = None
    filter_items: Optional[List[FilterSchema]] = None
    page_num: Optional[int] = 1
    items_per_page: Optional[int] = 20
    