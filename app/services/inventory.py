from sqlalchemy.orm import Session
from decimal import Decimal
from ..models import StockMovement, MovementType, Product

def current_stock(db: Session, product_id: int) -> Decimal:
    q = db.query(StockMovement).filter(StockMovement.product_id == product_id)
    total = Decimal(0)
    for m in q.all():
        if m.type == MovementType.IN:
            total += Decimal(m.qty)
        elif m.type == MovementType.OUT:
            total -= Decimal(m.qty)
        else:  # ADJUST
            total += Decimal(m.qty)  # negativo => baixa, positivo => aumento
    return total

def average_cost_after_in(db: Session, product_id: int, qty_in: Decimal, unit_cost: Decimal) -> Decimal:
    # custo médio simples: (estoque_atual*custo_médio_atual + entrada*custo_entrada) / (estoque_atual + entrada)
    # Para MVP, você pode snapshotar o unit_cost da última compra e usar isso.
    return unit_cost
