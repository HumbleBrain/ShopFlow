from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class PaymentCreate(BaseModel):
    commande_id: UUID
    montant: float = 0
    statut: Optional[bool] = None
    created_at:datetime
    
class PaymentRead(PaymentCreate):
    id: UUID

class PaymentUpdate(BaseModel):
    statut: Optional[bool]=None

 