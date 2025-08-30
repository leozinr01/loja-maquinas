from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal
from ..db import get_db
from ..models import StockMovement, MovementType, Product

router = APIRouter()

@router.post("/in")
def stock_in(product_id: int, qty: float, unit_cost: float | None = None, doc_ref: str | None = None, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(404, "Produto não encontrado")
    m = StockMovement(product_id=product_id, type=MovementType.IN, qty=Decimal(qty),
                      unit_cost=Decimal(unit_cost or product.cost_price), 
                      total_cost=Decimal(qty)*Decimal(unit_cost or product.cost_price),
                      doc_ref=doc_ref)
    db.add(m)
    db.commit()
    return {"ok": True, "movement_id": m.id}

@router.post("/out")
def stock_out(product_id: int, qty: float, doc_ref: str | None = None, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(404, "Produto não encontrado")
    m = StockMovement(product_id=product_id, type=MovementType.OUT, qty=Decimal(qty),
                      unit_cost=None, total_cost=None, doc_ref=doc_ref)
    db.add(m)
    db.commit()
    return {"ok": True, "movement_id": m.id}
