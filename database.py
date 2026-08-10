from sqlalchemy import sessionmaker,create_engine
db_url="postgresql://postgres:12345678@localhost:5432/mithil"
engine=create_engine(db_url)
local_session=sessionmaker(autocommit=False,autoflush=False,bind=engine)