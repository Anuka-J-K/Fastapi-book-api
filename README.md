# 📚 FastAPI Book Management API

A simple and efficient REST API built with **FastAPI** to manage a collection of books. This project demonstrates core FastAPI fundamentals including Routing, Pydantic validation, and Dependency Injection. It store new book details, update current ones, remove any. Also we can view the book details.

## 🚀 Features

- **CRUD Operations**: Create, Read, Update (Partial), and Delete books.
- **Data Validation**: Uses **Pydantic** schemas to ensure data integrity (e.g., ratings between 0-5).
- **Security**: Basic authentication simulation using **Dependency Injection**.
- **Interactive Docs**: Automatic documentation provided by Swagger UI.

## 🛠️ Tech Stack

- **FastAPI**: Modern, high-performance web framework.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: Lightning-fast ASGI server implementation.

## 🏁 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation at:
- **Swagger UI**: [http://127.0.0](http://127.0.0)

## 🔑 Usage Note
To perform **Create, Update, or Delete** operations, you must provide a query parameter `user_token=valid`.
