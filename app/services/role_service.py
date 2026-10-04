from uuid import UUID
from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.role import Role
from app.schemas.role import RoleCreate


def create_role(data: RoleCreate, session: Session) -> Role:
    role = Role.from_orm(data)
    session.add(role)
    session.commit()
    session.refresh(role)
    return role

def list_roles(session: Session) -> list[Role]:
    return session.exec(select(Role)).all()


def get_role_by_id(role_id: UUID, session: Session) -> Role: 
    item = session.get(Role, role_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role non trouvé")
    return item


def update_role(role_id: UUID, data: RoleCreate, session: Session) -> Role:  
    item = session.get(Role, role_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role non trouvé")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_role(role_id: UUID, session: Session) -> Role:        
    item = session.get(Role, role_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role non trouvé")
    session.delete(item)
    session.commit()
    return item