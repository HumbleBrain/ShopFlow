from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class OrderCreate(BaseModel):
    name: str
    product_id: UUID
    montant: float = 0
    statut: Optional[bool] = None
    created_at:datetime
    
class OrderRead(OrderCreate):
    id: UUID

class OrderUpdate(BaseModel):
    name: Optional[str]
    montant: Optional[float] 
    statut: Optional[bool] 