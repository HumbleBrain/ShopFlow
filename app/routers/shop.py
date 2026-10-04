from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import  Session, select
from app.core.database import get_session
from app.models.shop import Shop
from app.schemas.shop import ShopCreate, ShopRead, ShopUpdate
from app.services.shop_service import create_shop as create_shop_service, list_shops as list_shops_service, get_shop_by_id as get_shop_by_id_service, update_shop as update_shop_service, delete_shop as delete_shop_service
from uuid import UUID

router = APIRouter(prefix="/shop", tags=["Shop"])
@router.post("/", response_model=ShopRead,status_code=status.HTTP_201_CREATED)
def create_shop(data: ShopCreate, session: Session =Depends(get_session)):
    return create_shop_service(data,session)

@router.get("/", response_model=list[ShopRead])
def list_shop(session: Session = Depends(get_session)):
    return list_shops_service(session=session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{shop_id}", response_model=ShopRead)
def get_shop(shop_id: UUID, session: Session = Depends(get_session)):
    return get_shop_by_id_service(shop_id=shop_id, session=session)

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{shop_id}", response_model=ShopRead)
def update_shop(shop_id: UUID, data: ShopUpdate, session: Session = Depends(get_session)):
    return update_shop_service(shop_id=shop_id, data=data, session=session)

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{shop_id}", response_model=ShopRead)
def delete_shop(shop_id: UUID, session: Session = Depends(get_session)):
    return delete_shop_service(shop_id=shop_id, session=session)




