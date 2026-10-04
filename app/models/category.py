from uuid import UUID, uuid4

from sqlmodel import Relationship, SQLModel, Field 
from typing import TYPE_CHECKING, List, Optional 
from datetime import datetime

if TYPE_CHECKING:
   from app.models.product import Product 

class Category(SQLModel, table=True): 
    id: UUID = Field(default_factory=uuid4, primary_key=True) 
    name: Optional[str]  = Field(max_length=100, unique=True) 
    description: Optional[str] = None 
    created_at: Optional[datetime]  = Field(default_factory=datetime.utcnow) 

    products: List["Product"] = Relationship(back_populates="category")
