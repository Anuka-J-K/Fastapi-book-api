# This code demonstrates a simple FastAPI application with CRUD operations for managing books. 
# It includes Pydantic models for data validation, dependency injection for authentication, and asynchronous route handlers.

from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

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
books_db = [
    {"id": 1, "title": "Madol Duwa", "author": "Martin Wickramasinghe", "rating": 4.5},
    {"id": 2, "title": "Gamperaliya", "author": "Martin Wickramasinghe", "rating": 4.8}
]

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
async def get_all_books():# Async logic to fetch all books from the database
    return books_db

# CREATE: Add a new book (Requires Dependency)
@app.post("/books")
async def add_book(book: Book, token: str = Depends(is_logged_in)):
    books_db.append(book.model_dump())# Async logic to add a new book to the database
    return {"message": "Book added successfully"}

# UPDATE: Update an existing book (Requires Dependency)
# 2. PATCH Route: Updates only the fields you send in the request body
@app.patch("/books/{book_id}")
async def patch_book(book_id: int, update_data: BookUpdate, token: str = Depends(is_logged_in)):
    for book in books_db:
        if book["id"] == book_id:
            # Get only the fields that were actually sent in the request
            data = update_data.model_dump(exclude_unset=True)# Async logic to update the book details in the database
            
            # Update the book details with new data
            for key, value in data.items():# Update only the fields that were sent in the request
                book[key] = value
                
            return {"message": "Updated successfully", "updated_book": book}
            
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: Remove a book (Requires Dependency)
@app.delete("/books/{book_id}")
async def delete_book(book_id: int, token: str = Depends(is_logged_in)):
    # Async logic to find and remove the book
    for index, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db.pop(index)# Remove the book from the database
            return {"message": "Book deleted successfully"}
            
    raise HTTPException(status_code=404, detail="Book not found")

# Updated Schema for PATCH
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    rating: Optional[float] = Field(None, gt=0, le=5)

# PATCH: Update only specific fields
@app.patch("/books/{book_id}")
async def patch_book(book_id: int, update_data: BookUpdate, token: str = Depends(is_logged_in)): # Async logic to update only specific fields of a book in the database
    for book in books_db:
        if book["id"] == book_id:
            # model_dump(exclude_unset=True) is the key here
            data = update_data.model_dump(exclude_unset=True)
            for key, value in data.items():
                book[key] = value
            return {"message": "Updated successfully", "updated_book": book}
    raise HTTPException(status_code=404, detail="Book not found") # This route allows you to update only the fields you want by sending only those fields in the request body.
