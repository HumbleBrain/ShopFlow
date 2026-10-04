from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.category import Category
from app.schemas.category import CategoryCreate
from uuid import UUID


def ensure_category_name_is_unique(
    name: str,
    session: Session,
    excluded_category_id: UUID | None = None,
) -> None:
    statement = select(Category).where(Category.name == name)
    existing_category = session.exec(statement).first()

    if existing_category and existing_category.id != excluded_category_id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Une catégorie portant ce nom existe déjà",
        )


def create_category(data:CategoryCreate,session:Session)->Category:
    ensure_category_name_is_unique(data.name, session)
    category=Category.from_orm(data)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def list_categories(session:Session)->list[Category]:
    return session.exec(select(Category)).all()


def get_category_by_id(category_id:UUID,session:Session)->Category:
    item = session.get(Category, category_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catégorie non trouvée")
    return item


def update_category(category_id:UUID,data:CategoryCreate,session:Session)->Category:
    item = session.get(Category, category_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catégorie non trouvée")

    if data.name is not None:
        ensure_category_name_is_unique(data.name, session, excluded_category_id=category_id)
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def delete_category(category_id:UUID,session:Session)->Category:
    item = session.get(Category, category_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Catégorie non trouvée")
    session.delete(item)
    session.commit()
    return item

