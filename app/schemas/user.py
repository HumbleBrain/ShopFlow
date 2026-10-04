from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    prenom: str 
    telephone:str
    created_at: datetime 

class UserUpdate(BaseModel):
    # Les champs optionnels pour la mise à jour
    name: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    
class UserRead(UserCreate):
    id: UUID

