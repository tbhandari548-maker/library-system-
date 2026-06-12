# models.py
# Simple classes (models) to represent Book, Student, and Admin.
# Note: In this project we store data in JSON, so these classes are mainly for learning OOP.

class Book:
    def __init__(self, id: str, title: str, author: str, available_copies: int):
        self.id = id
        self.title = title
        self.author = author
        self.available_copies = available_copies


class Student:
    def __init__(self, name: str, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []


class Admin:
    # Admin is a special "role" in the system.
    # In this beginner project, if user types name = "admin", we treat them as admin.
    def __init__(self, name: str = "admin"):
        self.name = name 