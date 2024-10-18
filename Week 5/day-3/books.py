from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, StrictInt, Field
from typing import Optional

app = FastAPI()

class Book:
    def __init__(self, id, title, author, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.published_year = published_year

class BookRequest(BaseModel):
    id: Optional[StrictInt] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    published_year:StrictInt = Field(gt=1800, lt=2025)

BOOKS = [
    Book(1, "Book 1", "Author 1", 2020),
    Book(2, "Book 2", "Author 2", 2021),
    Book(3, "Book 3", "Author 3", 2022),
    Book(4, "Book 4", "Author 4", 2023),
    Book(5, "Book 5", "Author 5", 2024),
]

@app.get("/books")
async def getAllBooks():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")
        
@app.get("/books/")
async def read_book_by_year(published_year: int = Query(gt=1800, lt=2025)):
    books_to_return = []
    for book in BOOKS:
        if book.published_year == published_year:
            books_to_return.append(book)

    return books_to_return

@app.get("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(getBookId(new_book))
    return "New Book Record Created Successfully"

def getBookId(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id=1
    return book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")