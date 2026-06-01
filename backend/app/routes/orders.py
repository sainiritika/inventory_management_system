from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Customer, Product
from ..schemas import OrderCreate
from ..repositories import order_repo

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("",status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate,db: Session = Depends(get_db)):


    customer = (db.query(Customer).filter(Customer.id == order.customer_id).first())

    if not customer:
        raise HTTPException(status_code=404,detail="Customer not found")

  
    total_amount = 0

    for item in order.items:

       
        product = ( db.query(Product).filter(Product.id == item.product_id).first())

      
        if not product:
            raise HTTPException(status_code=404,detail=f"Product {item.product_id} not found")

       
        if product.stock_quantity < item.quantity:
            raise HTTPException(status_code=400,detail=f"Insufficient inventory for product {product.name}")

   
        total_amount += (product.price * item.quantity)

    created_order = (order_repo.create_order(db,order.customer_id,total_amount))

    for item in order.items:
        product = ( db.query(Product).filter(Product.id == item.product_id).first())

        product.stock_quantity -= item.quantity


        order_repo.create_order_item(db,created_order.id,item.product_id,item.quantity,product.price)

    db.commit()
    return {
        "message": "Order created successfully",
        "order_id": created_order.id,
        "customer_id": order.customer_id,
        "total_amount": total_amount
    }


@router.get("")
def get_orders(db: Session = Depends(get_db)):

    return (order_repo.get_orders(db))


@router.get("/{order_id}")
def get_order(order_id: int,db: Session = Depends(get_db)):

    order = (order_repo.get_order_by_id(db,order_id))

    if not order:
        raise HTTPException(status_code=404,detail="Order not found")

    return order


@router.delete("/{order_id}")
def delete_order(order_id: int,db: Session = Depends(get_db)):

    order = (order_repo.get_order_by_id(db,order_id))

    if not order:
        raise HTTPException(status_code=404,detail="Order not found")

    order_repo.delete_order(db,order)

    return { "message": "Order deleted successfully"}