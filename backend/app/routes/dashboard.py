from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from ..database import get_db

from ..repositories import dashboard_repo

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard(db: Session = Depends(get_db)):

    return {"total_products":dashboard_repo.total_products(db),"total_customers":dashboard_repo.total_customers(db),"total_orders":dashboard_repo.total_orders(db),"low_stock_products":dashboard_repo.low_stock_products(db)}