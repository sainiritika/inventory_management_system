from sqlalchemy.orm import Session

from ..models import Product

def create_product(db: Session,product):
    new_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock_quantity=product.stock_quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session):
    return db.query(Product).all()

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_sku(db: Session,sku: str):
    return db.query(Product).filter(Product.sku == sku).first()

def get_product_by_id(db: Session,product_id: int):
    return (db.query(Product).filter(Product.id == product_id).first())

def update_product(db: Session,product,updated):
    product.name = updated.name
    product.sku = updated.sku
    product.price = updated.price
    product.stock_quantity = updated.stock_quantity

    db.commit()

    db.refresh(product)

    return product

def delete_product(db: Session,product):

    db.delete(product)

    db.commit()


