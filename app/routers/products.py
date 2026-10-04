from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.product import Product
from uuid import UUID
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.services.products_services import create_product as create_product_service, list_products as list_products_service, get_product_by_id as get_product_by_id_service, update_product as update_product_service, delete_product as delete_product_service

router = APIRouter(prefix="/products", tags=["Products"])
@router.post("/", response_model=ProductRead,status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate, session: Session =Depends(get_session)):
    return create_product_service(data,session)

@router.get("/", response_model=list[ProductRead])
def list_products(session: Session = Depends(get_session)):
    return list_products_service(session=session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: UUID, session: Session = Depends(get_session)):
    return get_product_by_id_service(product_id=product_id, session=session)

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: UUID, data: ProductUpdate, session: Session = Depends(get_session)):
    return update_product_service(product_id=product_id, data=data, session=session)

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{product_id}", response_model=ProductRead)
def delete_product(product_id: UUID, session: Session = Depends(get_session)):
    return delete_product_service(product_id=product_id, session=session)