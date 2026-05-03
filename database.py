# database.py
from sqlalchemy import create_engine #create_engine is used to create a connection to the database
from sqlalchemy.ext.declarative import declarative_base #declarative_base is used to create a base class for our models
from sqlalchemy.orm import sessionmaker #sessionmaker is used to create a session factory

# Database file location
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()
