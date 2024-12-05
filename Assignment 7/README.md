# Problem Statement: Library Management System

Design a Library Management System using Object-Oriented Programming (OOP) concepts and Python's typing features. The system should support basic CRUD operations (Create, Read, Update, Delete) for books, manage different types of users (Librarians and Members), and handle book borrowing transactions with file-based data persistence. Appropriate error handling for file operations is required.

# Requirements:

1. Classes and Inheritance:
Create a base class User with common attributes such as user_id, name, and email.
Create two child classes:
Librarian: Should be able to manage (add, update, delete) books in the system.
Member: Should be able to borrow and return books.
2. Books:
Create a Book class with attributes such as book_id, title, author, and availability (a boolean indicating if the book is available or not).
Provide methods to display book information.
3. Library Management:
Create a LibraryManager class to handle CRUD operations for books and users. The class should:
Add, update, and delete books.
Borrow and return books for members.
Read and write book and user data to files.
4. File Handling:
Store book and user data in separate files (books.txt and users.txt).
Implement error handling for file operations (e.g., file not found, I/O errors).
5. Transactions:
Implement a method for members to borrow a book. When a book is borrowed, it should no longer be available for other users until it is returned.
Implement a method for members to return a book.
6. Encapsulation and Polymorphism:
Ensure that class attributes are properly encapsulated (use private attributes where necessary).
Use polymorphism where appropriate (e.g., methods that behave differently for Librarian and Member).
7. Static and Class Methods:
Use class methods to track the total number of books and users in the system.
Use static methods where appropriate for utility functions (e.g., validating user emails or checking book availability).