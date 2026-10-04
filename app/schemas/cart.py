from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class CartCreate(BaseModel):
    statut: str
    create_at: datetime
    
class CartRead(CartCreate):
    id: UUID

class CartUpdate(BaseModel):
    statut: Optional[str]