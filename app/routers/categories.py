from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.services.categories_services import create_category as create_category_service, list_categories as list_categories_service, get_category_by_id as get_category_by_id_service, update_category as update_category_service, delete_category as delete_category_service
from uuid import UUID

router = APIRouter(prefix="/category", tags=["Category"])
@router.post("/add/", response_model=CategoryRead,status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, session: Session =Depends(get_session)): #=Depends(get_session) permet d'acceder a la base de donnees
    return create_category_service(data,session)

@router.get("/list/", response_model=list[CategoryRead])
def list_categories(session: Session = Depends(get_session)):
    return list_categories_service(session=session)

# ============ NOUVEAU : GET par ID ============
@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: UUID, session: Session = Depends(get_session)):
    return get_category_by_id_service(category_id=category_id, session=session)

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: UUID, data: CategoryUpdate, session: Session = Depends(get_session)):
    return update_category_service(category_id=category_id, data=data, session=session)


# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{category_id}", response_model=CategoryRead)
def delete_category(category_id: UUID, session: Session = Depends(get_session)):
    return delete_category_service(category_id=category_id, session=session)