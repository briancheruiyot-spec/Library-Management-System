from lib.helpers import (
  list_libraries, create_library, delete_library, view_library_books,
  list_books, create_book, delete_book, 
  find_library_by_name, find_book_by_title, find_book_by_author,
  check_out_book, return_book, list_overdue_books, exit_program
)

def main():
  while True:
    print("\n--- Library Management System ---")
    print("1. Librarian Mode")
    print("2. Patron Mode")
    print("0. Exit")
    
    choice = input("> ").strip()
    
    if choice == "1":
      librarian_mode()
    elif choice == "2":
      patron_mode()
    elif choice == "0":
      exit_program()
    else:
      print("Invalid choice. Please try again.")

def librarian_mode():
  while True:
    print("\n--- Librarian Menu ---")
    print("1. List all libraries")
    print("2. Create a library")
    print("3. Delete a library")
    print("4. View books in a library")
    print("5. List all books")
    print("6. Create a book")
    print("7. Delete a book")
    print("8. Find library by name")
    print("9. Find book by title")
    print("10. Find book by author")
    print("11. List overdue books")
    print("0. Back to main menu")
    
    choice = input("> ").strip()
    
    actions = {
      "0": lambda: None,  # Just break out of the loop
      "1": list_libraries,
      "2": create_library,
      "3": delete_library,
      "4": view_library_books,
      "5": list_books,
      "6": create_book,
      "7": delete_book,
      "8": find_library_by_name,
      "9": find_book_by_title,
      "10": find_book_by_author,
      "11": list_overdue_books
    }
    
    if choice in actions:
      if choice == "0":
        return  # Return to main menu
      actions[choice]()
    else:
      print("Invalid choice. Please try again.")

def patron_mode():
  while True:
    print("\n--- Patron Menu ---")
    print("1. List all libraries")
    print("2. View books in a library")
    print("3. List all books")
    print("4. Find library by name")
    print("5. Find book by title")
    print("6. Find book by author")
    print("7. Check out a book")
    print("8. Return a book")
    print("0. Back to main menu")
    
    choice = input("> ").strip()
    
    actions = {
      "0": lambda: None,  # Just break out of the loop
      "1": list_libraries,
      "2": view_library_books,
      "3": list_books,
      "4": find_library_by_name,
      "5": find_book_by_title,
      "6": find_book_by_author,
      "7": check_out_book,
      "8": return_book
    }
    
    if choice in actions:
      if choice == "0":
        return  # Return to main menu
      actions[choice]()
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()