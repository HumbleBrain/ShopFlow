from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.user_role import User_Role
from app.schemas.user_role import UserRoleCreate, UserRoleRead
from app.services.user_role_service import assigne_role_to_user as assigne_role_to_user_service, list_user_roles as list_user_roles_service,remove_role_from_user as remove_role_from_user_service,check_user_role as check_user_role_service


router = APIRouter(prefix="/user_role", tags=["User_Role"])
@router.post("/", response_model=UserRoleRead,status_code=status.HTTP_201_CREATED)
def create_user_role(data: UserRoleCreate, session: Session =Depends(get_session)):
    return assigne_role_to_user_service(data=data, session=session)

@router.get("/{user_id}", response_model=list[UserRoleRead])
def list_user_role(user_id:UUID,session: Session = Depends(get_session)):
    return list_user_roles_service(user_id,session=session)

@router.delete("/", response_model=UserRoleRead)
def remove_role_from_user(user_id: UUID, role_id: UUID, session: Session = Depends(get_session)):
    return remove_role_from_user_service(user_id=user_id, role_id=role_id, session=session)

@router.get("/check", response_model=bool)
def check_user_role(user_id: UUID, role_id: UUID, session: Session = Depends(get_session)):
    return check_user_role_service(user_id=user_id, role_id=role_id, session=session)

