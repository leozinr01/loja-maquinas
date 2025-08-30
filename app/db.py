# Importa a função para criar conexão com o banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Define a URL do banco de dados a partir de uma variável de ambiente
DB_URL = os.getenv("DATABASE_URL", "sqlite:///./loja.db")
connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
engine = create_engine(DB_URL, echo=False, future=True, connect_args=connect_args)

# Cria uma fábrica de sessões (SessionLocal) para interagir com o banco
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

# Função utilitária para injetar uma sessão no FastAPI
def get_db():
    from fastapi import Depends
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
