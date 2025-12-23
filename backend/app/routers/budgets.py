from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Budget

router = APIRouter(prefix=/"budgets", tags=["budgets"])

@router.get("/")
def get_budget(db: Session = Depends(get_db)):
    budget = db.query(Budget).all()
    return {"budgets": budget}

