from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional,List
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
    from app.models.adress import Adress
    from app.models.order import Order
    from app.models.shop import Shop
    from app.models.shop_admin import ShopAdmin
    from app.models.user_role import User_Role


class User(SQLModel, table=True): 
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True) 
    name: str = Field(max_length=100, unique=True) 
    prenom: Optional[str] = None 
    telephone:Optional[str] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 

    user_roles:List["User_Role"]=Relationship(back_populates="user")
    orders:List["Order"]=Relationship(back_populates="user")
    adress:List["Adress"]=Relationship(back_populates="user")
    shops:List["Shop"]=Relationship(back_populates="creator")
    shopAdmins:List["ShopAdmin"]=Relationship(back_populates="user")

  