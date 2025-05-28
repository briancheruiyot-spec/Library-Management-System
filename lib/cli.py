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
  print("\n--- Library Management CLI ---")
  print("0. Exit")
  print("1. List all libraries")
  print("2. Create a library")
  print("3. Delete a library")
  print("4. View books in a library")
  print("5. List all books")
  print("6. Create a book")
  print("7. Delete a book")

if __name__ == "__main__":
  main()