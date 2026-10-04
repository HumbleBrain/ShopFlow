from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.schemas.cart import CartCreate, CartRead, CartUpdate
from app.services.cart_service import create_cart as create_cart_service, list_carts as list_carts_service, get_cart_by_id as get_cart_by_id_service, update_cart as update_cart_service, delete_cart as delete_cart_service

router = APIRouter(prefix="/cart", tags=["Cart"])
@router.post("/", response_model=CartRead,status_code=status.HTTP_201_CREATED)
def create_cart(data: CartCreate, session: Session =Depends(get_session)): #=Depends(get_session) permet d'acceder a la base de donnees
    return create_cart_service(data=data, session=session)

@router.get("/", response_model=list[CartRead])
def list_carts(session: Session = Depends(get_session)):
    return list_carts_service(session=session)


# ============ NOUVEAU : GET par ID ============
@router.get("/{cart_id}", response_model=CartRead)
def get_cart(cart_id: int, session: Session = Depends(get_session)):
    return get_cart_by_id_service(cart_id=cart_id, session=session)


# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{cart_id}", response_model=CartRead)
def update_cart(cart_id: int, data: CartUpdate, session: Session = Depends(get_session)):
    return update_cart_service(cart_id=cart_id, data=data, session=session)


# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{cart_id}", response_model=CartRead)
def delete_cart(cart_id: int, session: Session = Depends(get_session)):
    return delete_cart_service(cart_id=cart_id, session=session )
