from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from uuid import UUID
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleRead, RoleUpdate
from app.services.role_service import create_role as create_role_service, list_roles as list_roles_service, get_role_by_id as get_role_by_id_service, update_role as update_role_service, delete_role as delete_role_service

router = APIRouter(prefix="/role", tags=["Role"])
@router.post("/", response_model=RoleRead,status_code=status.HTTP_201_CREATED)
def create_role(data: RoleCreate, session: Session =Depends(get_session)):
    return create_role_service(data,session)

@router.get("/", response_model=list[RoleRead])
def list_roles(session: Session = Depends(get_session)):
    return list_roles_service(session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{role_id}", response_model=RoleRead)
def get_role(role_id: UUID, session: Session = Depends(get_session)):
    return get_role_by_id_service(role_id, session)

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{role_id}", response_model=RoleRead)
def update_role(role_id: UUID, data: RoleUpdate, session: Session = Depends(get_session)):
    return update_role_service(role_id=role_id, data=data, session=session)

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{role_id}", response_model=RoleRead)
def delete_role(role_id: UUID, session: Session = Depends(get_session)):
    return delete_role_service(role_id=role_id, session=session)
