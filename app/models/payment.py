from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional 
from datetime import datetime 
from uuid import UUID,uuid4

if TYPE_CHECKING:   
   from app.models.order import Order 


class Payment(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    order_id: UUID = Field(foreign_key="order.id") 
    montant: Optional[float] = None 
    statut:Optional[bool] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 
    
    order:Optional["Order"]=Relationship(back_populates="payments")