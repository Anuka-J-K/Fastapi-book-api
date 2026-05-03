# This code demonstrates a simple FastAPI application with CRUD operations for managing books. 
# It includes Pydantic models for data validation, dependency injection for authentication, and asynchronous route handlers.

from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from models import BookModel # Import the model
from database import SessionLocal, engine, Base # Import the database
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


app = FastAPI(title="Fast API Tutorial")#

# PYDANTIC SCHEMAS
# Defining how the data should look and validating it
class Book(BaseModel):
    id: int
    title: str
    author: str
    rating: float = Field(gt=0, le=5) # Validation: Rating must be 0-5

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    rating: Optional[float] = Field(None, gt=0, le=5)

# Temporary In-memory Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DEPENDENCY INJECTION 
# Reusable logic to check authentication before accessing certain routes
def is_logged_in(user_token: str = Query(...)):
    if user_token != "valid": # In real application, you would check the token against a database or authentication service
                            # For demonstration, we are just checking if the token is "valid" (user_token = valid)
        raise HTTPException(status_code=401, detail="Invalid Token")
    return user_token

# ROUTING & ASYNC/AWAIT

# READ: Get all books (Public route)
@app.get("/books", response_model=List[Book])
async def get_all_books(db: Session = Depends(get_db)): # Async logic to fetch all books from the database
    books = db.query(BookModel).all() # Query the database for all books
    return books

# CREATE: Add a new book (Requires Dependency)
@app.post("/books")
async def add_book(book: Book, db: Session = Depends(get_db), token: str = Depends(is_logged_in)): # Async logic to add a new book to the database
    new_book = BookModel(id = book.id, title = book.title, author = book.author, rating = book.rating) # create a new book instance
    db.add(new_book) # add the new book to the database
    db.commit() # commit the changes
    db.refresh(new_book) # refresh the new book
    return {"message": "Book added successfully" , "Book": new_book}

# UPDATE: Update an existing book (Requires Dependency)
# 2. PATCH Route: Updates only the fields you send in the request body
@app.patch("/books/{book_id}")
async def patch_book(book_id: int, update_data: BookUpdate, db: Session = Depends(get_db), token: str = Depends(is_logged_in)):
    # Query the book from the database
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    
    if db_book:
        # Get only the fields that were actually sent in the request
        data = update_data.model_dump(exclude_unset=True)
        
        # Update the book details with new data
        for key, value in data.items():
            setattr(db_book, key, value)
            
        db.commit()
        db.refresh(db_book)
        return {"message": "Updated successfully", "updated_book": db_book}
        
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: Remove a book (Requires Dependency)
@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(is_logged_in)):
    # Query the book from the database
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    
    if db_book:
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Book not found")
