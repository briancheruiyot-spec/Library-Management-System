# 📚 Library Management System

A simple yet powerful command-line interface (CLI) application for managing libraries and books using Python and SQLite. Built as part of the Flatiron Phase 3 project, this system enables you to perform CRUD operations on libraries and their associated books.

---

## 🚀 Features

- 📖 Add, view, delete books
- 🏛️ Add, view, delete libraries
- 🔍 Search for books by title or author
- 🔍 Search for libraries by name
- 🛠️ Built with SQLAlchemy and Alembic for database migrations
- 🐍 Pythonic CLI menu system

---

## 🗂️ Project Structure

Library-Management-System/
├── lib/
│ ├── cli.py # CLI entry point
│ ├── helpers.py # Reusable CLI functions
│ ├── models/
│ │ ├── init.py
│ │ ├── book.py
│ │ └── library.py
│ ├── db/
│ │ ├── base.py # SQLAlchemy base and engine
│ │ ├── session.py # Session factory
│ │ ├── seed.py # Script to seed the database
│ │ └── migrations/ # Alembic migrations
├── .gitignore
├── alembic.ini
└── README.md

---

## 🔧 Setup Instructions

### 1. 🐍 Create and activate a virtual environment

- pipenv install
- pipenv shell

### 2. 🛠️ Run Alembic migrations

alembic upgrade head

### 3. 🌱 Seed the database with initial data

python -m lib.db.seed

### 4. 💻 Run the CLI

python -m lib.cli

---

## 📋 CLI Options

--- Library Management CLI ---

0. Exit
1. List all libraries
2. Create a library
3. Delete a library
4. View books in a library
5. List all books
6. Create a book
7. Delete a book
8. Find library by name
9. Find book by title
10. Find book by author

---

## 📦 Dependencies

- Python
- pipenv
- SQLAlchemy
- Alembic

## 🙌 Contributing
Feel free to fork this repo, suggest features, or improve the CLI UI.

## 📜 License

This project is for educational use as part of the Flatiron School curriculum.

## 👨‍💻 Author

Developed by Brian Cheruiyot, briancheruiyot6@gmail.com.




