from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.user import User
from app.schemas import User
from app.schemas.user import UserCreate
from uuid import UUID


def create_user(data:UserCreate,session:Session)->User:
    user=User.from_orm(data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def list_users(session:Session)->list[User]:
    return session.exec(select(User)).all()


def get_user_by_id(user_id:UUID,session:Session)->User:
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User non trouvée")
    return user


def update_user(user_id:UUID,data:UserCreate,session:Session)->User:
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User non trouvée")
    
    # Mettre à jour uniquement les champs fournis
    user_data = data.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(user_id:UUID,session:Session)->User:        
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User non trouvée")
    session.delete(user)
    session.commit()
    return user