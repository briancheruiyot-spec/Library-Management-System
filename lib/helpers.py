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