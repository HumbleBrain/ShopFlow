from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.user_role import User_Role
from app.schemas.user_role import UserRoleCreate
from uuid import UUID

# Assigner un role à un utilisateur
def assigne_role_to_user(data:UserRoleCreate,session:Session)->User_Role:
    userRole=User_Role.from_orm(data)
    session.add(userRole)
    session.commit()
    session.refresh(userRole)
    return userRole

# la liste des roles assignés à un utilisateur
def list_user_roles(user_id:UUID,session:Session)->list[User_Role]:
    return session.exec(select(User_Role).where(User_Role.user_id == user_id)).all()

#retirer un role a un utilisateur
def remove_role_from_user(user_id:UUID,role_id: UUID, session: Session) -> User_Role:  
    item = session.get(User_Role,user_id, role_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ce role n'a pas ete assigne a cet utilisateur")
    session.delete(item)
    session.commit()
    return item

#Verifier la permission d'assignation
def check_user_role(user_id:UUID,role_id: UUID, session: Session) -> bool:
    item = session.get(User_Role,user_id, role_id)
    result = True if item else False     
    return result

