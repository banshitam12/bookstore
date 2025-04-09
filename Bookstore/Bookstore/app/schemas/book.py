from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    price: float
    rating: float
    published_date: date

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    category: Optional[str]
    price: Optional[float]
    rating: Optional[float]
    published_date: Optional[date]

class BookOut(BaseModel):
    id: int
    title: Optional[str]
    author: Optional[str]
    category: Optional[str]
    price: Optional[float]
    rating: Optional[float]
    published_date: Optional[date]

    class Config:
        orm_mode = True

