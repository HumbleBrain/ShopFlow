from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.cart_item import CartItem
from app.schemas.cart_item import CartItemCreate


def create_cart_item(user_id:UUID,data: CartItemCreate, session: Session) -> CartItem:
        cartItem = CartItem.from_orm(data)
        cartItem.user_id = user_id
        session.add(cartItem)
        session.commit()
        session.refresh(cartItem)
        return cartItem
    

def list_cart_items(user_id:UUID,session: Session) -> list[CartItem]:
    return session.exec(select(CartItem).where(CartItem.user_id == user_id)).all()


def get_cart_item_by_id(user_id:UUID,cartItem_id: UUID, session: Session) -> CartItem:
    item = session.exec(select(CartItem).where(CartItem.user_id == user_id, CartItem.id == cartItem_id)).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CartItem non trouvée")
    return item


def update_cart_item(cartItem_id: UUID,user_id:UUID, data: CartItemCreate, session: Session) -> CartItem:    
    item = session.get(CartItem, cartItem_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CartItem non trouvée")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_cart_item(cartItem_id: UUID,user_id:UUID, session: Session) -> CartItem:  
    item = session.get(CartItem, cartItem_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CartItem non trouvée")
    session.delete(item)
    session.commit()
    return item