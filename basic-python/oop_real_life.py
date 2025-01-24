# Library Management System using OOP

# Base class for books
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self._book_id = book_id  # Protected member
        self._checked_out = False

    def check_out(self):
        if not self._checked_out:
            self._checked_out = True
            return "Book checked out successfully."
        else:
            return "Book already checked out."

    def check_in(self):
        if self._checked_out:
            self._checked_out = False
            return "Book returned successfully."
        else:
            return "Book was not checked out."

    def __str__(self):
        return f"{self.title} by {self.author}"

# Inherited class for Fiction books
class Fiction(Book):
    def __init__(self, title, author, book_id, genre):
        super().__init__(title, author, book_id)
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author}, Genre: {self.genre}"

# Inherited class for Non-Fiction books
class NonFiction(Book):
    def __init__(self, title, author, book_id, subject):
        super().__init__(title, author, book_id)
        self.subject = subject

    def __str__(self):
        return f"{self.title} by {self.author}, Subject: {self.subject}"

# Example usage
fiction_book = Fiction("1984", "George Orwell", 1, "Dystopian")
non_fiction_book = NonFiction("A Brief History of Time", "Stephen Hawking", 2, "Science")

print(fiction_book)
print(non_fiction_book)
print(fiction_book.check_out())
print(fiction_book.check_in())
