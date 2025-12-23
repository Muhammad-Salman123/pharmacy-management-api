# Pharmacy Management API

A backend REST API built with FastAPI for managing pharmacy inventory and sales operations.

## 🚀 Features

- Medicine inventory management (CRUD)
- Stock tracking with validation
- Expiry date checks
- Sales transactions with business rules
- Low-stock and expired medicine insights
- Clean RESTful API design
- Interactive Swagger documentation

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## 📂 Project Structure

app/
├── models/
├── schemas/
├── routers/
├── database.py
├── main.py

## ▶️ How to Run Locally

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Run the server

pip install -r requirements.txt
uvicorn app.main:app --reload

## 📖 API Documentation

Once running, open:
http://127.0.0.1:8000/docs

## 💡 Learning Outcome

This project helped me understand real-world backend development including
API design, database modeling, business logic enforcement, and error handling.
