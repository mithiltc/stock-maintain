from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://localhost:12345@localhost:5432/mithil"

engine = create_engine(db_url)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
