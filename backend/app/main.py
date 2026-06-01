from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base
from .database import engine
from .routes import products,customers,orders,dashboard
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(dashboard.router)
app.include_router(orders.router)
app.include_router(products.router)
app.include_router(customers.router)
