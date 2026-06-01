from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from ..database import get_db
from app.schemas import ProductCreate,ProductUpdate
from ..repositories import product_repo
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)
    
@router.get("")
def get_products(db: Session = Depends(get_db)):
    return product_repo.get_products(db)

@router.post("",status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate,db: Session = Depends(get_db)):
    existing_product = (product_repo.get_product_by_sku(db,product.sku))
    if existing_product:
        raise HTTPException(status_code=400,detail="SKU already exists")

    return product_repo.create_product(db,product)

@router.get("/{product_id}")
def get_product(product_id: int,db: Session = Depends(get_db)):
    product = (product_repo.get_product_by_id(db,product_id))
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")

    return product

@router.put("/{product_id}")
def update_product(product_id: int,updated: ProductUpdate,db: Session = Depends(get_db)):
    product = (product_repo.get_product_by_id(db,product_id))
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    existing_product = (product_repo.get_product_by_sku(db,updated.sku))
    existing_product = (product_repo.get_product_by_sku(db,updated.sku))
    return (product_repo.update_product(db,product,updated))
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = (product_repo.get_product_by_id(db,product_id))
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    product_repo.delete_product(db,product)

    return {"message": "Product deleted successfully"}
