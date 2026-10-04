from sqlmodel import SQLModel, Field ,Relationship
from typing import TYPE_CHECKING, List, Optional 
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.shop_admin import ShopAdmin
    from app.models.user import User


class Shop(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    name: str = Field(max_length=100, unique=True) 
    description: Optional[str] = None 
    user_id:Optional[UUID]= Field(foreign_key="user.id") 

    creator:Optional["User"]=Relationship(back_populates="shops")
    products: List["Product"] = Relationship(back_populates="shop")
    shopAdmins:List["ShopAdmin"]=Relationship(back_populates="shop")




