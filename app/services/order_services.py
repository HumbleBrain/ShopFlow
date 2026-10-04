from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.order import Order
from app.schemas.order import OrderCreate
from uuid import UUID

def create_order(data:OrderCreate,session:Session)->Order:
    order=Order.from_orm(data)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def list_orders(session:Session)->list[Order]:
    return session.exec(select(Order)).all()


def get_order_by_id(order_id:UUID,session:Session)->Order:
    item = session.get(Order, order_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande non trouvée")
    return item


def update_order(order_id:UUID,data:OrderCreate,session:Session)->Order:
    item = session.get(Order, order_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande non trouvée")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_order(order_id:UUID,session:Session)->Order:
    item = session.get(Order, order_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commande non trouvée")
    session.delete(item)
    session.commit()
    return item




