from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class CartItemCreate(BaseModel):
    cart_id: UUID
    product_id:UUID
    quantity:int
    create_at: datetime
    
class CartItemRead(CartItemCreate):
    id: UUID

class CartItemUpdate(BaseModel):
    quantity: Optional[int] 



