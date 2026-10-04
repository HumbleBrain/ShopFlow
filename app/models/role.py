from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, List, Optional 
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
    from app.models.shop_admin import ShopAdmin
    from app.models.user_role import User_Role


class Role(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    name: str = Field(max_length=100, unique=True) 
    created_at: datetime = Field(default_factory=datetime.utcnow) 

    user_roles:List["User_Role"]=Relationship(back_populates="role")
