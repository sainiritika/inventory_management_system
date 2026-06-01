
from sqlalchemy.orm import Session

from ..models import Customer
def create_customer(db: Session,customer):

    new_customer = Customer(
        full_name=customer.full_name,
        email=customer.email,
        phone=customer.phone
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    return new_customer

def get_customers(db: Session):

    return db.query(Customer).all()

def get_customer_by_id(db: Session,customer_id: int):

    return db.query(Customer).filter(Customer.id == customer_id).first()
def get_customer_by_email(db: Session,email: str):
    return db.query(Customer).filter(Customer.email == email).first()

def delete_customer(db: Session,customer):

    db.delete(customer)

    db.commit()