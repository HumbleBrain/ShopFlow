from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0
    category_id: UUID = None
    
class ProductRead(ProductCreate):
    id: UUID

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float]=None
    stock: Optional[int] = 0
    category_id: Optional[UUID] = None