from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.shop_admin import ShopAdmin
from app.schemas.shop_admin import ShopAdminCreate, ShopAdminRead
from app.services.shop_admin_service import create_shop_admin as create_shop_admin_service, list_shop_admins as list_shop_admins_service

router = APIRouter(prefix="/ShopAdmin", tags=["ShopAdmin"])
@router.post("/", response_model=ShopAdminRead,status_code=status.HTTP_201_CREATED)
def create_shopAdmin(data: ShopAdminCreate, session: Session =Depends(get_session)):
    return create_shop_admin_service(data=data, session=session)

@router.get("/{shop_id}", response_model=list[ShopAdminRead])
def list_shopAdmins(shop_id: UUID, session: Session = Depends(get_session)):
    return list_shop_admins_service(shop_id=shop_id, session=session)