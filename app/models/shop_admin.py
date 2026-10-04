from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional 
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
    from app.models.user import User 
    from app.models.shop import Shop


class ShopAdmin(SQLModel, table=True): 
    shop_id: Optional[UUID] = Field(foreign_key="shop.id", primary_key=True) 
    user_id: Optional[UUID] = Field(foreign_key="user.id", primary_key=True) 
    role: Optional[str]=None

    #Permet d'acceder aux proprietes de chacunes des classes
    user:Optional["User"]=Relationship(back_populates="shopAdmins") 
    shop:Optional["Shop"]=Relationship(back_populates="shopAdmins")






