from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255))
    category = Column(String(100))
    price = Column(Float)
    rating = Column(Float)
    published_date = Column(Date)

