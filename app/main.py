from fastapi import FastAPI
from .db import Base, engine
from .routers import products, stock, sales, purchases, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loja de Máquinas API")

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(stock.router, prefix="/stock", tags=["stock"])
app.include_router(sales.router, prefix="/sales", tags=["sales"])
app.include_router(purchases.router, prefix="/purchases", tags=["purchases"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
