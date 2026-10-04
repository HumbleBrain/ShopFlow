from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.shop_admin import ShopAdmin
from app.schemas.shop_admin import ShopAdminCreate
from uuid import UUID

def create_shop_admin(data:ShopAdminCreate,session:Session)->ShopAdmin:
    shopAdmin=ShopAdmin.from_orm(data)
    session.add(shopAdmin)
    session.commit()
    session.refresh(shopAdmin)
    return shopAdmin

def list_shop_admins(shop_id:UUID,session:Session)->list[ShopAdmin]:
    return session.exec(select(ShopAdmin).where(ShopAdmin.shop_id == shop_id)).all()