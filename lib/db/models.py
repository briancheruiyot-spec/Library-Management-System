from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///lib/db/library.db')
Session = sessionmaker(bind=engine)
session = Session()


class Library(Base):
  __tablename__ = 'libraries'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  books = relationship('Book', back_populates='library', cascade='all, delete')

  def __repr__(self):
    return f"<Library(id={self.id}, name='{self.name}')>"
  
class Book(Base):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  library_id = Column(Integer, ForeignKey('libraries.id'))

  library = relationship('Library', back_populates='books')

  def __repr__(self):
    return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
  
