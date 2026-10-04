from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ShopCreate(BaseModel):
    name: str
    description: str
    user_id: UUID

class ShopRead(ShopCreate):
    id: UUID

class ShopUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

