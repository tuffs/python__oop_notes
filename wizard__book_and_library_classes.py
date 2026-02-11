# This is a Book and Library Class set where the
# library methods were defined by what an assignment
# called for. A difficult labeled assignment.

# This code is great!

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        keep_books = []
        for f_book in self.books:
            if f_book.title != book.title and f_book.author != book.author:
                keep_books.append(f_book)

        self.books = keep_books

    def search_books(self, search_string):
        found_books = []
        search_string = search_string.lower()
        for book in self.books:
            author = book.author.lower()
            title = book.title.lower()
            if search_string in author or search_string in title:
                found_books.append(book)

        return found_books
