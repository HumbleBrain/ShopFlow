from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.adress import Adress
from app.schemas.adress import AdressCreate


def create_adress(user_id:int,data: AdressCreate, session: Session) -> Adress:
    adress = Adress.from_orm(data)
    adress.user_id = user_id
    session.add(adress)
    session.commit()
    session.refresh(adress)
    return adress


def list_adresses(user_id:int,session: Session) -> list[Adress]:
    return session.exec(select(Adress).where(Adress.user_id == user_id)).all()


def get_adress_by_id(user_id:int,adress_id: int, session: Session) -> Adress:
    item = session.exec(select(Adress).where(Adress.user_id == user_id, Adress.id == adress_id)).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adresse non trouvée")
    return item


def update_adress(adress_id: int,user_id:int, data: AdressCreate, session: Session) -> Adress:
    item = session.get(Adress, adress_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adresse non trouvée")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_adress(adress_id: int,user_id:int, session: Session) -> Adress:  
    item = session.get(Adress, adress_id,user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adresse non trouvée")
    session.delete(item)
    session.commit()
    return item