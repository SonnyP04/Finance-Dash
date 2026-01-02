from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Budget
from pydantic import BaseModel

router = APIRouter(prefix="/budgets", tags=["budgets"])

class CreateBudget(BaseModel):
    limit : int 
    category : str 
    month : str 

@router.get("/")
async def get_all_budgets(db: Session = Depends(get_db)):
    budget = db.query(Budget).all()
    return {"budgets": budget}

@router.post("/")
async def create_budget(budget : CreateBudget, db: Session = Depends(get_db)):
    newBudget = Budget(**budget.dict())
    db.add(newBudget)
    db.commit()
    db.refresh(newBudget)
    return newBudget

@router.get("/{budget_id}")
async def get_budget(budget_id: int, db: Session = Depends(get_db)):
    budget = db.query(Budget).filter(Budget.id == budget_id).first()
    return budget



    
