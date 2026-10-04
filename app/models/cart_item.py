from ast import List
from uuid import UUID,uuid4
from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional 
from datetime import datetime 

if TYPE_CHECKING:
    from app.models.cart import Cart
    from app.models.product import Product 

class CartItem(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    cart_id: Optional[UUID] = Field(foreign_key="cart.id")
    product_id: Optional[UUID] = Field(foreign_key="product.id")
    quantity:Optional[int] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 
    
    cart:Optional["Cart"]=Relationship(back_populates="cartItems")
    product:Optional["Product"]=Relationship(back_populates="cartItems")




    