from fastapi import FastAPI
from sqlalchemy.orm import Session

from backend.database.db import SessionLocal
from backend.database.models import Book

app = FastAPI(
    title="Library MCP Server"
)

@app.get("/")
def root():

    return {
        "server": "Library MCP",
        "status": "running"
    }

@app.get("/search")
def search_book(query: str):

    db: Session = SessionLocal()

    books = db.query(Book).filter(
        Book.title.ilike(f"%{query}%")
    ).all()

    return [
        {
            "title": book.title,
            "author": book.author,
            "copies": book.available_copies,
            "shelf": book.shelf
        }
        for book in books
    ]

@app.get("/all_books")
def all_books():

    db: Session = SessionLocal()

    books = db.query(Book).all()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "copies": book.available_copies,
            "shelf": book.shelf
        }
        for book in books
    ]
    
@app.get("/available")
def available_books():

    db: Session = SessionLocal()

    books = db.query(Book).filter(
        Book.available_copies > 0
    ).all()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "copies": book.available_copies
        }
        for book in books
    ]
    
@app.get("/book/{book_id}")
def get_book(book_id: int):

    db: Session = SessionLocal()

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        return {
            "error": "Book not found"
        }

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "copies": book.available_copies,
        "shelf": book.shelf
    }
    
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "library_mcp"
    }