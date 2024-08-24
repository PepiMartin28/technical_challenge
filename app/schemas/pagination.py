from pydantic import BaseModel
from typing import List, Any

class PaginationSchema(BaseModel):
    total_pages: int
    page: int
    items_per_page: int
    total_items: int
    data: List[Any]

