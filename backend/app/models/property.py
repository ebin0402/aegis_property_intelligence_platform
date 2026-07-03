# PostGIS model
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    location = Column(String)
    bedrooms = Column(Integer)
