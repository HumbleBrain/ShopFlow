from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/user", tags=["User"])
@router.post("/", response_model=UserRead,status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, session: Session =Depends(get_session)): #=Depends(get_session) permet d'acceder a la base de donnees
    item = User.from_orm(data)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.get("/", response_model=list[UserRead])
def list_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()


# ============ NOUVEAU : GET par ID ============
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, session: Session = Depends(get_session)):
    item = session.get(User, user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    return item

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: UUID, data: UserUpdate, session: Session = Depends(get_session)):
    item = session.get(User, user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: UUID, session: Session = Depends(get_session)):
    item = session.get(User, user_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    session.delete(item)
    session.commit()
    return item