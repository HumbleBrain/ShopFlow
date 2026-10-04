from sqlmodel import SQLModel, Field ,Relationship
from typing import TYPE_CHECKING, Optional 
from datetime import datetime
from uuid import UUID,uuid4

if TYPE_CHECKING:
   from app.models.user import User 

class Adress(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    user_id:UUID =Field( foreign_key="user.id") 
    street: Optional[str] = None 
    city: Optional[str] = None 
    zip_code: Optional[str] = None 
    country: Optional[str] = None 
    type: Optional[str] = None 
    created_at: datetime = Field(default_factory=datetime.utcnow) 

    #Permet d'acceder aux proprietes de chacunes des classes
    user:Optional["User"]=Relationship(back_populates="adress") 
