from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class CategoryCreate(BaseModel):
    name: str
    description: str
    created_at:datetime

    
class CategoryRead(CategoryCreate):
    id: UUID

class CategoryUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str] 
    created_at: Optional[datetime]
