from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .db import Base

class MovementType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"
    ADJUST = "ADJUST"

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    sku = Column(String(60), unique=True, nullable=True)
    name = Column(String(200), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    unit = Column(String(20), default="UN")
    cost_price = Column(Numeric(12,2), default=0)
    sale_price = Column(Numeric(12,2), default=0)
    min_stock = Column(Numeric(12,3), default=0)
    barcode = Column(String(60), unique=True, nullable=True)
    is_active = Column(Boolean, default=True)

    category = relationship("Category")

class StockMovement(Base):
    __tablename__ = "stock_movements"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    type = Column(Enum(MovementType), nullable=False)
    qty = Column(Numeric(12,3), nullable=False)
    unit_cost = Column(Numeric(12,2), nullable=True)   # para IN/ADJUST+
    total_cost = Column(Numeric(12,2), nullable=True)
    doc_ref = Column(String(120), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("Product")

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    cnpj_cpf = Column(String(20))
    phone = Column(String(30))
    email = Column(String(120))

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    cpf_cnpj = Column(String(20))
    phone = Column(String(30))
    email = Column(String(120))

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Numeric(12,2), default=0)
    supplier = relationship("Supplier")
    items = relationship("PurchaseItem", cascade="all, delete-orphan", backref="purchase")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"
    id = Column(Integer, primary_key=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    qty = Column(Numeric(12,3), nullable=False)
    unit_cost = Column(Numeric(12,2), nullable=False)

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Numeric(12,2), default=0)
    payment_method = Column(String(30))  # dinheiro, pix, cartão
    customer = relationship("Customer")
    items = relationship("SaleItem", cascade="all, delete-orphan", backref="sale")

class SaleItem(Base):
    __tablename__ = "sale_items"
    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    qty = Column(Numeric(12,3), nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)
    unit_cost_snapshot = Column(Numeric(12,2))  # custo médio no momento da venda

class CashMovement(Base):
    __tablename__ = "cash_movements"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    type = Column(String(10))  # IN / OUT
    amount = Column(Numeric(12,2), nullable=False)
    origin = Column(String(20))  # SALE, PURCHASE, ADJUST
    ref_id = Column(Integer, nullable=True)
    notes = Column(String(255))
