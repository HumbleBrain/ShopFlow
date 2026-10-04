from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class AdressCreate(BaseModel):
    user_id: UUID
    street: str
    city: str
    zip_code: str
    country: str
    type: str
    created_at: datetime 
    
class AdressRead(AdressCreate):
    id: UUID

class AdressUpdate(BaseModel):
    street: Optional[str]
    city:  Optional[str]
    zip_code:  Optional[str]
    country:  Optional[str]
    type:  Optional[str]
    