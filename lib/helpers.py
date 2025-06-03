from lib.db.models import get_session, Library, Book
from datetime import datetime

def get_valid_input(prompt, validator=None, error_msg="Invalid input"):
  while True:
    try:
      value = input(prompt).strip()
      if validator:
        value = validator(value)
      return value
    except ValueError as e:
      print(f"Error: {e}")

def validate_id(input_str):
  if not input_str.isdigit():
    raise ValueError("ID must be a number")
  return int(input_str)

def list_libraries():
  session = get_session()
  try:
    libs = Library.get_all(session)
    if not libs:
      print("No libraries found")
      return
    for lib in libs:
      print(lib)
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def create_library():
  session = get_session()
  try:
    name = get_valid_input("Enter library name: ")
    Library.create(session, name)
    print("Library created successfully!")
  except Exception as e:
    session.rollback()
    print(f"Error creating library: {e}")
  finally:
    session.close()

def delete_library():
  list_libraries()
  session = get_session()
  try:
    lib_id = get_valid_input("Enter library ID to delete: ", validate_id)
    if Library.delete(session, lib_id):
      print("Library deleted successfully!")
    else:
      print("Library not found")
  except Exception as e:
    session.rollback()
    print(f"Error deleting library: {e}")
  finally:
    session.close()

def view_library_books():
  list_libraries()
  session = get_session()
  try:
    lib_id = get_valid_input("Enter library ID to view books: ", validate_id)
    lib = Library.find_by_id(session, lib_id)
    if lib:
      if lib.books:
        for book in lib.books:
          status = "Checked out" if book.checked_out else "Available"
          print(f"{book} - Status: {status}")
      else:
        print("No books found in this library")
    else:
      print("Library not found")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def list_books():
  session = get_session()
  try:
    books = Book.get_all(session)
    if books:
      for book in books:
        status = "Checked out" if book.checked_out else "Available"
        print(f"{book} - Status: {status}")
    else:
      print("No books found")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def create_book():
  list_libraries()
  session = get_session()
  try:
    title = get_valid_input("Enter book title: ")
    author = get_valid_input("Enter author name: ")
    lib_id = get_valid_input("Enter library ID: ", validate_id)
    
    if not Library.find_by_id(session, lib_id):
      raise ValueError("Library does not exist")
      
    Book.create(session, title, author, lib_id)
    print("Book created successfully!")
  except Exception as e:
    session.rollback()
    print(f"Error creating book: {e}")
  finally:
    session.close()

def delete_book():
  list_books()
  session = get_session()
  try:
    book_id = get_valid_input("Enter book ID to delete: ", validate_id)
    if Book.delete(session, book_id):
      print("Book deleted successfully!")
    else:
      print("Book not found")
  except Exception as e:
    session.rollback()
    print(f"Error deleting book: {e}")
  finally:
    session.close()

def find_library_by_name():
  session = get_session()
  try:
    name = input("Enter library name to search: ").strip()
    results = Library.find_by_name(session, name)
    if results:
      for lib in results:
        print(lib)
    else:
      print("No libraries found")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def find_book_by_title():
  session = get_session()
  try:
    title = input("Enter book title to search: ").strip()
    results = Book.find_by_title(session, title)
    if results:
      for book in results:
        status = "Checked out" if book.checked_out else "Available"
        print(f"{book} - Status: {status}")
    else:
      print("No books found")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def find_book_by_author():
  session = get_session()
  try:
    author = input("Enter author name to search: ").strip()
    results = Book.find_by_author(session, author)
    if results:
      for book in results:
        status = "Checked out" if book.checked_out else "Available"
        print(f"{book} - Status: {status}")
    else:
      print("No books found")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def check_out_book():
  list_books()
  session = get_session()
  try:
    book_id = get_valid_input("Enter book ID to check out: ", validate_id)
    patron_name = get_valid_input("Enter patron name: ")
    
    if Book.check_out(session, book_id, patron_name):
      print("Book checked out successfully!")
      book = Book.find_by_id(session, book_id)
      print(f"Due date: {book.due_date.strftime('%Y-%m-%d')}")
    else:
      print("Book not found")
  except Exception as e:
    session.rollback()
    print(f"Error checking out book: {e}")
  finally:
    session.close()

def return_book():
  list_books()
  session = get_session()
  try:
    book_id = get_valid_input("Enter book ID to return: ", validate_id)
    if Book.return_book(session, book_id):
      print("Book returned successfully!")
    else:
      print("Book not found")
  except Exception as e:
    session.rollback()
    print(f"Error returning book: {e}")
  finally:
    session.close()

def list_overdue_books():
  session = get_session()
  try:
    overdue_books = Book.get_overdue(session)
    if not overdue_books:
      print("No overdue books found")
      return
      
    print("\n--- Overdue Books ---")
    for book in overdue_books:
      days_overdue = (datetime.now() - book.due_date).days
      print(f"ID: {book.id}, Title: {book.title}")
      print(f"Patron: {book.patron_name}")
      print(f"Due date: {book.due_date.strftime('%Y-%m-%d')} ({days_overdue} days overdue)")
      print("-" * 40)
  except Exception as e:
    print(f"Error: {e}")
  finally:
    session.close()

def exit_program():
  print("Goodbye!")
  exit()