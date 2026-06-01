from sqlalchemy.orm import Session

from ..models import (Order,OrderItem)
def create_order(db,customer_id,total_amount):

    order = Order(customer_id=customer_id,total_amount=total_amount)

    db.add(order)

    db.commit()

    db.refresh(order)

    return order

def create_order_item(db,order_id,product_id,quantity,price):

    item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price
    )

    db.add(item)

    db.commit()

    return item

def get_orders(db):

    return db.query(Order).all()

def get_order_by_id(db,order_id):

    return db.query(Order).filter(Order.id == order_id).first()

def delete_order(db,order):

    db.delete(order)

    db.commit()