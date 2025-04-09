from fastapi import FastAPI
from app.routers import auth, books
from app.database import engine
from app.models import user, book

app = FastAPI()

@app.get("/")
def root():
    return {"message": "📚 Welcome to the Bookstore API!"}

# Create database tables
user.Base.metadata.create_all(bind=engine)
book.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(books.router, prefix="/books", tags=["Books"])
