
from uuid import UUID, uuid4

from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional,List
from datetime import datetime

if TYPE_CHECKING:
    from app.models.cart_item import CartItem
    from app.models.order import Order


class Cart(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True)  
    statut:Optional[bool] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 
    
    orders:List["Order"]=Relationship(back_populates="cart")
    cartItems:List["CartItem"]=Relationship(back_populates="cart")




    