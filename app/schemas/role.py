from datetime import datetime

from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class RoleCreate(BaseModel):
    name: str
    created_at: datetime

class RoleRead(RoleCreate):
    id: UUID

class RoleUpdate(BaseModel):
    name: Optional[str] = None
