from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Transaction

router = APIRouter(prefix="/transaction", tags=["transaction"])

@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@router.get('/{id}')
def get_transaction(id: int, db: Session = Depends(get_db)):
    transaction_id = db.query(Transaction).filter(Transaction.id == id).first()
    return transaction_id



