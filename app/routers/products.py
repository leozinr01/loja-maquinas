from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Product

router = APIRouter()

@router.get("/")
def list_products(q: str | None = None, db: Session = Depends(get_db)):
    qs = db.query(Product)
    if q:
        like = f"%{q}%"
        qs = qs.filter(Product.name.ilike(like))
    return qs.order_by(Product.name).all()

@router.post("/")
def create_product(data: dict, db: Session = Depends(get_db)):
    p = Product(**data)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
