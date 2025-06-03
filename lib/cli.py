from lib.helpers import (
  list_libraries, create_library, delete_library, view_library_books,
  list_books, create_book, delete_book, exit_program,
  find_library_by_name, find_book_by_title, find_book_by_author,
  check_out_book, return_book, list_overdue_books
)

def main():
  while True:
    menu()
    choice = input("> ").strip()
    
    actions = {
      "0": exit_program,
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
      "11": check_out_book,
      "12": return_book,
      "13": list_overdue_books
    }
    
    if choice in actions:
      actions[choice]()
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
  print("8. Find library by name")
  print("9. Find book by title")
  print("10. Find book by author")
  print("11. Check out a book")
  print("12. Return a book")
  print("13. List overdue books")

if __name__ == "__main__":
  main()