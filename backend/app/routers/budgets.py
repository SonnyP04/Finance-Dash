from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Budget

router = APIRouter(prefix="/budgets", tags=["budgets"])

@router.get("/")
async def get_all_budgets(db: Session = Depends(get_db)):
    budget = db.query(Budget).all()
    return {"budgets": budget}

#@router.post("/budget/")
#async def create_budget(budget: Budget):

@router.get("/{budget_id}")
async def get_budget(id: int, budget: Budget, Session = Depends(get_db)):
    budget = db.query(budget).filter(budget.id == id).first()
    return budget



    
