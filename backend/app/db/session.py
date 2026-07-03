from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://aegis:aegis@db:5432/aegis"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
