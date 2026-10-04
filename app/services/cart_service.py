from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.cart import Cart
from app.schemas.cart import CartCreate

def create_cart(user_id:UUID,data: CartCreate, session: Session) -> Cart:
    cart = Cart.from_orm(data)
    cart.user_id = user_id
    session.add(cart)
    session.commit()
    session.refresh(cart)
    return cart

def list_carts(user_id:UUID,session: Session) -> list[Cart]:
    return session.exec(select(Cart).where(Cart.user_id == user_id)).all()

def get_cart_by_id(user_id:UUID,cart_id: UUID, session: Session) -> Cart:
    item = session.exec(select(Cart).where(Cart.user_id == user_id, Cart.id == cart_id)).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart non trouvée")
    return item

def update_cart(cart_id: UUID,user_id:UUID, data: CartCreate, session: Session) -> Cart:
    item = session.get(Cart, cart_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart non trouvée")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def delete_cart(cart_id: UUID,user_id:UUID, session: Session) -> Cart:  
    item = session.get(Cart, cart_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart non trouvée")
    session.delete(item)
    session.commit()
    return item