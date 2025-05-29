from faker import Faker
import random
from .models import get_session, Library, Book
from sqlalchemy.exc import IntegrityError

fake = Faker()

def seed():
  session = get_session()
  try:
    session.query(Book).delete()
    session.query(Library).delete()
    session.commit()

    # Create 3 libraries
    for _ in range(3):
      while True:
        name = fake.company()
        try:
          lib = Library.create(session, name)
          break
        except ValueError as e:
          print(f"Validation error creating library: {e}")
        except IntegrityError as e:
          session.rollback()
          print(f"Integrity error creating library: {e}")

      # Create 2-5 books per library
      for _ in range(random.randint(2, 5)):
        title = fake.sentence(nb_words=3)[:100]
        author = fake.name()
        try:
          Book.create(session, title, author, lib.id)
        except ValueError as e:
          print(f"Skipping book: {e}")
        except IntegrityError as e:
          session.rollback()
          print(f"Integrity error creating book: {e}")

    print("Database seeded successfully!")

  except Exception as e:
    session.rollback()
    print(f"Unexpected error during seeding: {e}")
  finally:
    session.close()


if __name__ == "__main__":
  seed()
