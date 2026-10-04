from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from app.services.order_services import create_order as create_order_service, list_orders as list_orders_service, get_order_by_id as get_order_by_id_service, update_order as update_order_service, delete_order as delete_order_service 

router = APIRouter(prefix="/order", tags=["Order"])
@router.post("/", response_model=OrderRead,status_code=status.HTTP_201_CREATED)
def create_order(data: OrderCreate, session: Session =Depends(get_session)):
    return create_order_service(data,session)

@router.get("/", response_model=list[OrderRead])
def list_orders(session: Session = Depends(get_session)):
    return list_orders_service(session=session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, session: Session = Depends(get_session)):
    return get_order_by_id_service(order_id=order_id, session=session)

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{order_id}", response_model=OrderRead)
def update_order(order_id: int, data: OrderUpdate, session: Session = Depends(get_session)):
    return update_order_service(order_id=order_id, data=data, session=session)

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{order_id}", response_model=OrderRead)
def delete_order(order_id: int, session: Session = Depends(get_session)):
    return delete_order_service(order_id=order_id, session=session)