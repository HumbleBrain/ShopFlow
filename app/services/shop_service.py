from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.shop import Shop
from app.schemas.shop import ShopCreate
from uuid import UUID


def create_shop(data:ShopCreate,session:Session)->Shop:
    shop=Shop.from_orm(data)
    session.add(shop)
    session.commit()
    session.refresh(shop)
    return shop


def list_shops(session:Session)->list[Shop]:
    return session.exec(select(Shop)).all() 


def get_shop_by_id(shop_id:UUID,session:Session)->Shop:  
    item = session.get(Shop, shop_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shop non trouvé")
    return item


def update_shop(shop_id:UUID,data:ShopCreate,session:Session)->Shop:     
    item = session.get(Shop, shop_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shop non trouvé")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_shop(shop_id:UUID,session:Session)->Shop:  
    item = session.get(Shop, shop_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shop non trouvé")
    session.delete(item)
    session.commit()
    return item