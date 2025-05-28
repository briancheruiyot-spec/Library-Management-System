from lib.db.models import session, Library, Book

def list_libraries():
  libs = session.query(Library).all()
  for lib in libs:
    print(lib)

def create_library():
  name = input("Enter library name: ")
  if name:
    lib = Library(name=name)
    session.add(lib)
    session.commit()
    print("Library created.")

def delete_library():
  list_libraries()
  lib_id = input("Enter library ID to delete: ")
  lib = session.query(Library).get(lib_id)
  if lib:
    session.delete(lib)
    session.commit()
    print("Library deleted.")
  else:
    print("Library not found.")


def view_library_books():
  list_libraries()
  lib_id = input("Enter library ID to view books: ")
  lib = session.query(Library).get(lib_id)
  if lib:
    for book in lib.books:
      print(book)
  else:
    print("Library not found.")

def list_books():
  books = session.query(Book).all()
  for book in books:
    print(book)

def create_book():
  list_libraries()
  title = input("Enter book title: ")
  author = input("Enter author name: ")
  library_id = input("Enter library ID: ")
  if title and author and library_id:
    book = Book(title=title, author=author, library_id=library_id)
    session.add(book)
    session.commit()
    print("Book created.")

def delete_book():
  list_books()
  book_id = input("Enter book ID to delete: ")
  book = session.query(Book).get(book_id)
  if book:
    session.delete(book)
    session.commit()
    print("Book deleted.")
  else:
    print("Book not found.")

def exit_program():
  print("Goodbye!")
  exit()