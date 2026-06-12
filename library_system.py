# library_system.py
# All the business logic for the library lives here.
# Student actions: show books, borrow, return
# Admin actions: add, delete, update

from library.storage import load_books, save_books, load_students, save_students


class LibrarySystem:
    def __init__(self):
        self.books = load_books()
        self.students = load_students() 

    def _find_book(self, book_id): 
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def _book_id_exists(self, book_id):
        return self._find_book(book_id) is not None

    def get_student(self, name):
        # If student already exists, return it
        for student in self.students:
            if student["name"].lower() == name.lower():
                return student

        # Otherwise, create a new student record
        new_student = {"name": name, "borrowed_books": []}
        self.students.append(new_student)
        return new_student

    # --------------------
    # Student functions
    # --------------------
    def show_books(self):
        print("\nAvailable Books:")
        if not self.books:
            print("No books in library.")
            return

        for book in self.books:
            print(f"{book['id']} - {book['title']} by {book['author']} (Available: {book['available_copies']})")

    def show_student_status(self, student_name):
        student = self.get_student(student_name)
        print(f"\n{student['name']}, your borrowed books: {student['borrowed_books']}")

    def borrow_book(self, student_name, book_id):
        student = self.get_student(student_name)

        # Simple rule: max 2 books per student
        if len(student["borrowed_books"]) >= 2:
            print("You already have 2 books. Return one before borrowing.")
            return

        book = self._find_book(book_id)
        if book is None:
            print("Invalid Book ID.")
            return

        if book["available_copies"] <= 0:
            print("Book is not available right now.")
            return

        # Borrow
        book["available_copies"] -= 1
        student["borrowed_books"].append(book_id)

        # Save
        save_books(self.books)
        save_students(self.students)

        print("Book borrowed successfully!")

    def return_book(self, student_name, book_id):
        student = self.get_student(student_name)

        if book_id not in student["borrowed_books"]:
            print("You don't have this book.")
            return

        book = self._find_book(book_id)
        if book is None:
            # Very rare: book deleted by admin while student had it.
            # We'll still remove it from student record.
            student["borrowed_books"].remove(book_id)
            save_students(self.students)
            print("Book returned (note: book record was missing).")
            return

        # Return
        student["borrowed_books"].remove(book_id)
        book["available_copies"] += 1

        # Save
        save_books(self.books)
        save_students(self.students)

        print("Book returned successfully!")

    # --------------------
    # Admin functions
    # --------------------
    def admin_add_book(self, book_id, title, author, copies):
        if self._book_id_exists(book_id):
            print("This Book ID already exists. Use a different ID.")
            return

        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "available_copies": copies
        }
        self.books.append(new_book)
        save_books(self.books)
        print("Book added successfully!")

    def admin_delete_book(self, book_id):
        book = self._find_book(book_id)
        if book is None:
            print("Book ID not found.")
            return

        self.books.remove(book)
        save_books(self.books)
        print("Book deleted successfully!")

    def admin_update_copies(self, book_id, new_copies):
        book = self._find_book(book_id)
        if book is None:
            print("Book ID not found.")
            return

        # We only update available copies for simplicity
        book["available_copies"] = new_copies
        save_books(self.books)
        print("Copies updated successfully!")