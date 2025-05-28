from faker import Faker
from models import Base, engine, session, Library, Book
import random

fake = Faker()

def seed():
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)

def seed():
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)

  for _ in range(3):
    lib = Library(name=fake.company())
    session.add(lib)
    session.flush()

    for _ in range(random.randint(2, 5)):
      book = Book(
        title=fake.sentence(nb_words=3),
        author=fake.name(),
        library_id=lib.id
      )
      session.add(book)

  session.commit()
  print("Database seeded successfully!")