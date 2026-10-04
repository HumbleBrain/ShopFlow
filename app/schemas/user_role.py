from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserRoleCreate(BaseModel):
    user_id: UUID
    role_id: UUID
    created_at:datetime
    
class UserRoleRead(UserRoleCreate):
    user_id: UUID
    role_id: UUID


