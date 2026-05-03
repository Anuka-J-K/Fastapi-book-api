from sqlalchemy import Column, Integer, String, Float # Column is used to define the column name and type, Integer, String and Float are the data types
from database import Base # Base is the base class for all the models

class BookModel(Base): # class BookModel is the model for the book
    __tablename__ = "books" # table name

    id = Column(Integer, primary_key=True, index=True) # id is the primary key and index
    title = Column(String) # title of the book
    author = Column(String) # author_name of the book
    rating = Column(Float) # Rating should be decimal
