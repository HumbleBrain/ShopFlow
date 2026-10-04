from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentRead, PaymentUpdate

router = APIRouter(prefix="/payment", tags=["Payment"])
@router.post("/", response_model=PaymentRead,status_code=status.HTTP_201_CREATED)
def create_paiement(data: PaymentCreate, session: Session =Depends(get_session)):
    idem = Payment.from_orm(data)
    session.add(idem)
    session.commit()
    session.refresh(idem)
    return idem

@router.get("/", response_model=list[PaymentRead])
def list_payment(session: Session = Depends(get_session)):
    return session.exec(select(Payment)).all()

# ============ NOUVEAU : GET par ID ============
@router.get("/{payment_id}", response_model=PaymentRead)
def get_payment(payment_id: int, session: Session = Depends(get_session)):
    item = session.get(Payment, payment_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produit non trouvé")
    return item

# ============ NOUVEAU : PUT (UPDATE) ============
@router.put("/{payment_id}", response_model=PaymentRead)
def update_payment(payment_id: int, data: PaymentUpdate, session: Session = Depends(get_session)):
    item = session.get(Payment, payment_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paiement non trouvé")
    
    # Mettre à jour uniquement les champs fournis
    item_data = data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)
    
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# ============ NOUVEAU : DELETE par ID ============
@router.delete("/{payment_id}", response_model=PaymentRead)
def delete_payment(payment_id: int, session: Session = Depends(get_session)):
    item = session.get(Payment, payment_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paiement non trouvé")
    session.delete(item)
    session.commit()
    return item