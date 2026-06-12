# ui.py
# Handles user interaction (input/output).
# If user types name = "admin", they will see the admin menu.

from library.library_system import LibrarySystem


def _student_menu(library: LibrarySystem, student_name: str):
    while True:
        print("\n--- Student Menu ---")
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. My Borrowed Books")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.show_books()

        elif choice == "2":
            book_id = input("Enter Book ID to borrow (example: B001): ").strip()
            library.borrow_book(student_name, book_id)

        elif choice == "3":
            book_id = input("Enter Book ID to return (example: B001): ").strip()
            library.return_book(student_name, book_id)

        elif choice == "4":
            library.show_student_status(student_name)

        elif choice == "5":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Try again.")


def _admin_menu(library: LibrarySystem):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Show Books")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Update Copies")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.show_books()

        elif choice == "2":
            book_id = input("New Book ID (example: B010): ").strip()
            title = input("Book Title: ").strip()
            author = input("Author Name: ").strip()

            copies_str = input("Available copies (number): ").strip()
            if not copies_str.isdigit():
                print("Copies must be a number.")
                continue

            library.admin_add_book(book_id, title, author, int(copies_str))

        elif choice == "3":
            book_id = input("Book ID to delete: ").strip()
            library.admin_delete_book(book_id)

        elif choice == "4":
            book_id = input("Book ID to update copies: ").strip()
            copies_str = input("New available copies (number): ").strip()
            if not copies_str.isdigit():
                print("Copies must be a number.")
                continue

            library.admin_update_copies(book_id, int(copies_str))

        elif choice == "5":
            print("Exiting admin mode.")
            break

        else:
            print("Invalid choice. Try again.")


def start():
    print("Welcome to the Library System!")
    name = input("Enter your name (type 'admin' for admin mode): ").strip()

    library = LibrarySystem()

    if name.lower() == "admin":
        _admin_menu(library)
    else:
        _student_menu(library, name)