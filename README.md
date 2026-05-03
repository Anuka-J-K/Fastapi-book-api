# 📚 FastAPI Book Management API (with SQLite)

A simple and efficient REST API built with **FastAPI** to manage a collection of books. This project demonstrates core FastAPI fundamentals including Routing, Pydantic validation, Dependency Injection, and permanent data storage using **SQLAlchemy** and **SQLite**.

## 🚀 Features

- **Full CRUD Operations**: Create, Read, Update (Partial/PATCH), and Delete books.
- **Permanent Storage**: Data is stored securely in a local **SQLite** database (`books.db`).
- **Data Validation**: Uses **Pydantic** schemas to ensure data integrity (e.g., ratings between 0-5).
- **ORM Integration**: Uses **SQLAlchemy** for efficient database management and clean code.
- **Interactive Docs**: Automatic documentation provided by Swagger UI.

## 🛠️ Tech Stack

- **FastAPI**: Modern, high-performance web framework.
- **SQLAlchemy**: Powerful Python SQL toolkit and ORM.
- **SQLite**: Lightweight disk-based database.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: Lightning-fast ASGI server implementation.

## 🏁 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com
cd Fastapi-book-api
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation at:
- **Swagger UI**: [http://127.0.0](http://127.0.0)

## 🔑 Usage Note
To perform **Create, Update, or Delete** operations, you must provide a query parameter: `user_token=valid`
