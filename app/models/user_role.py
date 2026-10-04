from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, Optional 
from datetime import datetime
from uuid import UUID,uuid4

from app.models.role import Role
from app.models.user import User


class User_Role(SQLModel, table=True): 
    user_id: Optional[UUID] = Field(foreign_key="user.id", primary_key=True) 
    role_id: Optional[UUID] = Field(foreign_key="role.id", primary_key=True) 
    created_at: datetime = Field(default_factory=datetime.utcnow)  

    #Permet d'acceder aux proprietes de chacunes des classes
    user:Optional["User"]=Relationship(back_populates="user_roles") 
    role:Optional["Role"]=Relationship(back_populates="user_roles")

    
