# Library Management System using Object-Oriented Programming

# Base class for books
class Book:
    # Constructor for the Book class
    def __init__(self, title, author, book_id):
        """
        Constructor for the Book class
        
        Parameters:
        title (str): Title of the book¯
        author (str): Author of the book
        book_id (int): ID of the book
        
        Initializes the title, author, book_id, and checked_out status of the book
        """

        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self._book_id = book_id  # Private: ID of the book
        self._checked_out = False  # Private: Status of the book, False means not checked out

    # Method to check out a book
    def check_out(self):
        if not self._checked_out:
            self._checked_out = True  # Mark the book as checked out
            return "Book checked out successfully"
        else:
            return "Book already checked out"  # Return message if the book is already checked out

    # Method to check in a book
    def check_in(self):
        if self._checked_out:
            self._checked_out = False  # Mark the book as not checked out
            return "Book returned successfully"
        else:
            return "Book was not checked out"  # Return message if the book was not checked out

    # String representation of the Book class
    def __str__(self):
        return f"{self.title} by {self.author}"  # Format the string to show book details

# Inherited class for Fiction books
class Fiction(Book):
    # Constructor for the Fiction class
    def __init__(self, title, author, book_id, genre):
        super().__init__(title, author, book_id)  # Call the constructor of the parent class
        self.genre = genre  # Genre of the book

    # String representation of the Fiction class
    def __str__(self):
        return f"{self.title} by {self.author}, Genre: {self.genre}"  # Format the string to show fiction book details

# Inherited class for Non-Fiction books
class NonFiction(Book):
    # Constructor for the NonFiction class
    def __init__(self, title, author, book_id, subject):
        super().__init__(title, author, book_id)  # Call the constructor of the parent class
        self.subject = subject  # Subject of the book

    # String representation of the NonFiction class
    def __str__(self):
        return f"{self.title} by {self.author}, Subject: {self.subject}"  # Format the string to show non-fiction book details

# Example usage
fiction_book = Fiction("1984", "Manish", 1, "The journey of success")
non_fiction_book = NonFiction("A Brief Story of my life in Tech", "Manjeet saw", 2, "The journey of Tech")

print(fiction_book)
print(non_fiction_book)
print(fiction_book.check_out())
print(fiction_book.check_in())
