from helpers import (
  list_libraries, create_library, delete_library, view_library_books,
  list_books, create_book, delete_book, exit_program
)

def main():
  while True:
    menu()
    choice = input("> ").strip()

    if choice == "0":
      exit_program()
    elif choice == "1":
      list_libraries()
    elif choice == "2":
      create_library()
    elif choice == "3":
      delete_library()
    elif choice == "4":
      view_library_books()
    elif choice == "5":
      list_books()
    elif choice == "6":
      create_book()
    elif choice == "7":
      delete_book()
    else:
      print("Invalid choice. Please try again.")

def menu():
  pass