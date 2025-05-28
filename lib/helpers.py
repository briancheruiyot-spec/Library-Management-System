from lib.db.models import session, Library, Book

def list_libraries():
  libs = session.query(Library).all()
  for lib in libs:
    print(lib)

