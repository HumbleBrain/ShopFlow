from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.adress import Adress
from app.schemas.adress import AdressCreate, AdressRead, AdressUpdate
from app.services.adress_service import create_adress as create_adress_service, list_adresses as list_adresses_service, get_adress_by_id as get_adress_by_id_service, update_adress as update_adress_service, delete_adress as delete_adress_service

router = APIRouter(prefix="/adress", tags=["Adress"])
@router.post("/{user_id}", response_model=AdressRead,status_code=status.HTTP_201_CREATED)
def create_adress(user_id: int, data: AdressCreate, session: Session =Depends(get_session)): #=Depends(get_session) permet d'acceder a la base de donnees
    return create_adress_service(user_id=user_id, data=data, session=session)

@router.get("/", response_model=list[AdressRead])
def list_adress(user_id: int, session: Session = Depends(get_session)):
    return list_adresses_service(user_id=user_id, session=session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{adress_id}", response_model=AdressRead)
def get_adress(user_id: int,adress_id: int, session: Session = Depends(get_session)):
    return get_adress_by_id_service( user_id=user_id,adress_id=adress_id, session=session)


# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{adress_id}", response_model=AdressRead)
def update_adress(adress_id: int, user_id: int, data: AdressUpdate, session: Session = Depends(get_session)):
    return update_adress_service(adress_id=adress_id, user_id=user_id, data=data, session=session)


# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{adress_id}", response_model=AdressRead)
def delete_adress(adress_id: int, user_id: int, session: Session = Depends(get_session)):
    return delete_adress_service(adress_id=adress_id, user_id=user_id, session=session)