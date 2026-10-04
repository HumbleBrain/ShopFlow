from sqlmodel import SQLModel, Field ,Relationship
from typing import TYPE_CHECKING, List, Optional 
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
    from app.models.cart_item import CartItem
    from app.models.category import Category
    from app.models.order import Order
    from app.models.shop import Shop


class Product(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    name: str = Field(max_length=200) 
    description: Optional[str] = None 
    price: float = Field(gt=0) 
    stock: int = Field(ge=0) 
    category_id: Optional[UUID] = Field(foreign_key="category.id") 
    shop_id: Optional[UUID] = Field(foreign_key="shop.id") 
    created_at: datetime = Field(default_factory=datetime.utcnow) 
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    category:Optional["Category"]=Relationship(back_populates="products") 
    shop:Optional["Shop"]=Relationship(back_populates="products") 
    cartItems:List["CartItem"]=Relationship(back_populates="product") 
    orders:List["Order"]=Relationship(back_populates="product") 
    


    