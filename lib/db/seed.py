from faker import Faker
import random
from .models import Base, engine, get_session, Library, Book
from sqlalchemy.exc import IntegrityError

fake = Faker()

def seed():
  try:
    session = get_session()
    
    # Clear existing data
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Create libraries
    for _ in range(3):
      name = fake.company()
      while True:
        try:
          lib = Library.create(session, name)
          break
        except ValueError as e:
          print(f"Validation error: {e}")
          name = fake.company()
      
      # Create books for library
      for _ in range(random.randint(2, 5)):
        title = fake.sentence(nb_words=3)[:100]
        author = fake.name()
        try:
          Book.create(session, title, author, lib.id)
        except ValueError as e:
          print(f"Skipping book: {e}")

    print("Database seeded successfully!")
  except IntegrityError as e:
    session.rollback()
    print(f"Seeding error: {e}")
  except Exception as e:
    session.rollback()
    print(f"Unexpected error: {e}")
  finally:
    session.close()

if __name__ == "__main__":
  seed()