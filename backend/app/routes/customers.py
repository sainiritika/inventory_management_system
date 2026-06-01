from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import CustomerCreate
from ..repositories import customer_repo

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)
@router.post("")
def create_customer(customer: CustomerCreate,db: Session = Depends(get_db)):

    existing_customer = (customer_repo.get_customer_by_email(db, customer.email))

    if existing_customer:
        raise HTTPException(status_code=400,detail="Email already exists")

    return (customer_repo.create_customer(db,customer))

@router.get("")
def get_customers(db: Session = Depends(get_db)):

    return customer_repo.get_customers(db)

@router.get("/{customer_id}")
def get_customer(customer_id: int,db: Session = Depends(get_db)):

    customer = (customer_repo.get_customer_by_id(db,customer_id))

    if not customer:
        raise HTTPException(status_code=404,detail="Customer not found")

    return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int,db: Session = Depends(get_db)):

    customer = (customer_repo.get_customer_by_id(db,customer_id))

    if not customer:
        raise HTTPException(status_code=404,detail="Customer not found")

    customer_repo.delete_customer(db,customer)

    return {"message": "Customer deleted"}