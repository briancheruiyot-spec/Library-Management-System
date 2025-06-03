# 📚 Library Management System

A powerful command-line interface (CLI) application for managing libraries and books using Python and SQLite. This system enables librarians and patrons to manage library resources efficiently with role-based access control.

## 🚀 Enhanced Features

### Role-based Access Control:

👩‍💼 Librarian Mode: Full CRUD operations for libraries and books

👤 Patron Mode: Book search, checkout, and return functionality

### Advanced Book Management:

- 📖 Add new books with validation

- 🔍 Search books by title or author

- ✅ Track book availability status

### Checkout System:

- 🛒 Check out books with automatic due date calculation (14 days)

- 🔙 Return books to make them available again

- ⏰ Track overdue books with days-overdue calculation

### Database Management:

- 🗄️ SQLite database with SQLAlchemy ORM

- 🔄 Alembic for database migrations

- 🌱 Seeding with realistic test data

## 🗂️ Project Structure

Library-Management-System/ ├── lib/ │ ├── cli.py # CLI entry point │ ├── helpers.py # Reusable CLI functions │ ├── models/ │ │ ├── init.py │ │ ├── book.py │ │ └── library.py │ ├── db/ │ │ ├── base.py # SQLAlchemy base and engine │ │ ├── session.py # Session factory │ │ ├── seed.py # Script to seed the database │ │ └── migrations/ # Alembic migrations ├── .gitignore ├── alembic.ini └── README.md

## 🔧 Setup Instructions

### 1. 🐍 Create and activate a virtual environment
- pipenv install
- pip install alembic
- pipenv shell

### 2. 🛠️ Run Alembic migrations
- alembic upgrade head

### 3. 🌱 Seed the database with initial data
- python -m lib.db.seed

### 4. 💻 Run the CLI
- python -m lib.cli


## 📋 Role-Based CLI Options

### 👩‍💼 Librarian Menu

--- Librarian Menu ---
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
11. List overdue books
0. Back to main menu

### 👤 Patron Menu

--- Patron Menu ---
1. List all libraries
2. View books in a library
3. List all books
4. Find library by name
5. Find book by title
6. Find book by author
7. Check out a book
8. Return a book
0. Back to main menu

## 📦 Dependencies
- Python
- SQLAlchemy (ORM)
- Alembic (Database migrations)
- Faker (Test data generation)
- pipenv (Dependency management)

## 🙌 Contributing
Feel free to fork this repo, suggest features, or improve the CLI UI. Contributions are welcome!


## 👨‍💻 Author
Developed by Brian Cheruiyot
Contact: briancheruiyot6@gmail.com