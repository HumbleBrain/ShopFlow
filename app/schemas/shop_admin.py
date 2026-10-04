from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ShopAdminCreate(BaseModel):
    shop_id:UUID
    user_id: UUID
    role: str
    
class ShopAdminRead(ShopAdminCreate):
    shop_id:UUID
    user_id: UUID
    role: Optional[str]

