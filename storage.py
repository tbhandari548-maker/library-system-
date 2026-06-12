# storage.py
# Responsible for reading and writing JSON files (books + students)

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")


def load_books():
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)


def load_students():
    with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(students):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)

def save_pawan():
    print('Pawan')
