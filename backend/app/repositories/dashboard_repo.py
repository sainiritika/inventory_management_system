from sqlalchemy.orm import Session

from ..models import (Product,Customer,Order)
def total_products(db: Session):

    return db.query(Product).count()

def total_customers(db: Session):

    return db.query(Customer).count()

def total_orders(db: Session):

    return db.query(Order).count()

def low_stock_products(db: Session):

    return db.query(Product).filter(Product.stock_quantity < 5).count()