from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud
from app.schemas.book import BookCreate, BookOut, BookUpdate
from app.models import Book
from app.auth.jwt_handler import get_current_user
from app.database import get_db
from typing import Optional, List

router = APIRouter()

@router.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.book.create_book(db=db, book=book)

@router.get("/books/", response_model=list[BookOut])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.book.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/books/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud.book.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/books/{book_id}", response_model=BookOut)
def update_book(
    book_id: int,
    book: BookUpdate,  # <- Use the partial schema
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    updated_book = crud.book.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/books/{book_id}", response_model=BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    deleted_book = crud.book.delete_book(db, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book

@router.get("/books/", response_model=List[BookOut])
def list_books(
    author: Optional[str] = None,
    category: Optional[str] = None,
    rating: Optional[float] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Book)

    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if category:
        query = query.filter(Book.category.ilike(f"%{category}%"))
    if rating:
        query = query.filter(Book.rating == rating)
    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))

    return query.all()

