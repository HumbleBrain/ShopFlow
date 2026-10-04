from sqlmodel import SQLModel, Field ,Relationship
from typing import TYPE_CHECKING, List, Optional 
from datetime import datetime
from uuid import UUID,uuid4
if TYPE_CHECKING:
    from app.models.cart import Cart
    from app.models.payment import Payment
    from app.models.product import Product
    from app.models.user import User


class Order(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    product_id: Optional[UUID] = Field(foreign_key="product.id") 
    cart_id: Optional[UUID] = Field(foreign_key="cart.id")
    user_id: Optional[UUID] = Field(foreign_key="user.id")  
    montant: Optional[float] = None 
    statut:Optional[bool] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 

    #Permet d'acceder aux proprietes de chacunes des classes
    user:Optional["User"]=Relationship(back_populates="orders") 
    cart:Optional["Cart"]=Relationship(back_populates="orders") 
    product:Optional["Product"]=Relationship(back_populates="orders") 
    payments:List["Payment"]=Relationship(back_populates="order") 
