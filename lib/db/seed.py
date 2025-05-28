from faker import Faker
from models import Base, engine, session, Library, Book
import random

fake = Faker()

def seed():
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)