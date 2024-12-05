from typing import List, Optional
import os

# Base Class: User
class User():
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}', email='{self.email}')"


# Derived Class: Librarian
class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

    def manage_books(self, library_manager):
        return library_manager

# Derived Class: Member
class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self.borrowed_books = []

    def borrow_book(self, library_manager, book_id: int):
        if library_manager.borrow_book(self, book_id):
            self.borrowed_books.append(book_id)
            print(f"{self.name} borrowed the book with ID {book_id}")

    def return_book(self, library_manager, book_id: int):
        if library_manager.return_book(self, book_id):
            self.borrowed_books.remove(book_id)
            print(f"{self.name} returned the book with ID {book_id}")


# Book Class
class Book():
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Availability: {availability}"


# Library Manager Class
class LibraryManager():
    def __init__(self):
        self.books_file = 'books.txt'
        self.users_file = 'users.txt'
        self.books = []
        self.users = []
        self.load_books()
        self.load_users()

    # CRUD operations for Books
    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None):
        for book in self.books:
            if book.book_id == book_id:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                print(f"Book with ID {book_id} updated successfully.")
                return
        print(f"Book with ID {book_id} not found.")

    def delete_book(self, book_id: int):
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    # Book Borrowing
    def borrow_book(self, member: Member, book_id: int) -> bool:
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                self.save_books()
                return True
        print(f"Book with ID {book_id} is not available for borrowing.")
        return False

    # Book Returning
    def return_book(self, member: Member, book_id: int) -> bool:
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                self.save_books()
                return True
        print(f"Book with ID {book_id} was not borrowed.")
        return False

    # File Handling
    def save_books(self):
        try:
            with open(self.books_file, 'w') as f:
                for book in self.books:
                    f.write(f"{book.book_id},{book.title},{book.author},{book.available}\n")
        except IOError:
            print("Error saving books to file.")

    def load_books(self):
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, 'r') as f:
                    for line in f:
                        book_id, title, author, available = line.strip().split(',')
                        self.books.append(Book(int(book_id), title, author, available == 'True'))
            except IOError:
                print("Error loading books from file.")

    def save_users(self):
        try:
            with open(self.users_file, 'w') as f:
                for user in self.users:
                    f.write(f"{user.user_id},{user.name},{user.email}\n")
        except IOError:
            print("Error saving users to file.")

    def load_users(self):
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    for line in f:
                        user_id, name, email = line.strip().split(',')
                        self.users.append(User(int(user_id), name, email))
            except IOError:
                print("Error loading users from file.")


# Example of usage
library_manager = LibraryManager()

# Adding books to the library
librarian = Librarian(1, "Libby", "libby@example.com")
librarian.manage_books(library_manager).add_book(Book(101, "1984", "George Orwell"))
librarian.manage_books(library_manager).add_book(Book(102, "Brave New World", "Aldous Huxley"))

# Member borrowing and returning books
member = Member(2, "Alice", "alice@example.com")
member.borrow_book(librarian.manage_books(library_manager), 101)
member.return_book(librarian.manage_books(library_manager), 101)

# Display all books
for book in library_manager.books:
  print(book.display_info())
