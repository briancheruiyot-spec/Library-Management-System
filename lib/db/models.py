from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, validates
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()
engine = create_engine('sqlite:///lib/db/library.db')
Session = sessionmaker(bind=engine)

def get_session():
  return Session()

class Library(Base):
  __tablename__ = 'libraries'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False, unique=True)
  books = relationship('Book', back_populates='library', cascade='all, delete')

  @validates('name')
  def validate_name(self, key, name):
    if not name or len(name.strip()) < 3:
      raise ValueError("Library name must be at least 3 characters")
    return name.strip()

  def __repr__(self):
    return f"<Library(id={self.id}, name='{self.name}')>"
  
  # ORM methods
  @classmethod
  def create(cls, session, name):
    library = cls(name=name)
    session.add(library)
    session.commit()
    return library

  @classmethod
  def delete(cls, session, id):
    library = session.get(cls, id)
    if library:
      session.delete(library)
      session.commit()
      return True
    return False

  @classmethod
  def get_all(cls, session):
    return session.query(cls).all()
  
  @classmethod
  def find_by_id(cls, session, id):
    return session.get(cls, id)
  
  @classmethod
  def find_by_name(cls, session, name):
    return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()

class Book(Base):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  library_id = Column(Integer, ForeignKey('libraries.id'))

  library = relationship('Library', back_populates='books')

  @validates('title', 'author')
  def validate_text(self, key, value):
    if not value or len(value.strip()) < 2:
      raise ValueError(f"{key.capitalize()} must be at least 2 characters")
    return value.strip()

  def __repr__(self):
    return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
  
  # ORM methods
  @classmethod
  def create(cls, session, title, author, library_id):
    book = cls(title=title, author=author, library_id=library_id)
    session.add(book)
    session.commit()
    return book

  @classmethod
  def delete(cls, session, id):
    book = session.get(cls, id)
    if book:
      session.delete(book)
      session.commit()
      return True
    return False

  @classmethod
  def get_all(cls, session):
    return session.query(cls).all()
  
  @classmethod
  def find_by_id(cls, session, id):
    return session.get(cls, id)
  
  @classmethod
  def find_by_title(cls, session, title):
    return session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
  
  @classmethod
  def find_by_author(cls, session, author):
    return session.query(cls).filter(cls.author.ilike(f"%{author}%")).all()