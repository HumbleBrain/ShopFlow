from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.cart_item import CartItemCreate, CartItemRead, CartItemUpdate
from app.services.cart_item_service import create_cart_item as create_cart_item_service, list_cart_items as list_cart_items_service, get_cart_item_by_id as get_cart_item_by_id_service, update_cart_item as update_cart_item_service, delete_cart_item as delete_cart_item_service 



router = APIRouter(prefix="/cart_item", tags=["CartItem"])
@router.post("/", response_model=CartItemRead,status_code=status.HTTP_201_CREATED)
def create_cart(data: CartItemCreate, session: Session =Depends(get_session)): #=Depends(get_session) permet d'acceder a la base de donnees
    return create_cart_item_service(data=data, session=session)


@router.get("/", response_model=list[CartItemRead])
def list_cartItems(session: Session = Depends(get_session)):
    return list_cart_items_service(session=session)


# ============ NOUVEAU : GET par ID ============
@router.get("/{cartItem_id}", response_model=CartItemRead)
def get_cartItem(cartItem_id: int, session: Session = Depends(get_session)):
    return get_cart_item_by_id_service(cartItem_id=cartItem_id, session=session)


# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{cartItem_id}", response_model=CartItemRead)
def update_cartItem(cartItem_id: int, data: CartItemUpdate, session: Session = Depends(get_session)):
    return update_cart_item_service(cartItem_id=cartItem_id, data=data, session=session)


# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{cartItem_id}", response_model=CartItemRead)
def delete_cartItem(cartItem_id: int, session: Session = Depends(get_session)):
    return delete_cart_item_service(cartItem_id=cartItem_id, session=session)





    