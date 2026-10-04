from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.product import Product
from app.schemas.product import ProductCreate
from uuid import UUID


def create_product(data:ProductCreate,session:Session)->Product:
    product=Product.from_orm(data)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def list_products(session:Session)->list[Product]:
    return session.exec(select(Product)).all()


def get_product_by_id(product_id:UUID,session:Session)->Product:
    item = session.get(Product, product_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produit non trouvé")
    return item


def update_product(product_id:UUID,data:ProductCreate,session:Session)->Product:
    item = session.get(Product, product_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produit non trouvé")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_product(product_id:UUID,session:Session)->Product:
    item = session.get(Product, product_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produit non trouvé")
    session.delete(item)
    session.commit()
    return item
