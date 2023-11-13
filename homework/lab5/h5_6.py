#Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD, and Magazine. Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_item(self):
        self.checked_out = False

    def __str__(self):
        return f"{self.name} ,  {self.author} ,  {self.year} ,  Checked Out: {self.checked_out}"

class Book(LibraryItem):
    def __init__(self, name, author, year, pages):
        super().__init__(name, author, year)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} ,  {self.pages} pages"

class DVD(LibraryItem):
    def __init__(self, name, author, year, runtime):
        super().__init__(name, author, year)
        self.runtime = runtime

    def __str__(self):
        return f"{super().__str__()} ,  {self.runtime} minutes"

class Magazine(LibraryItem):
    def __init__(self, name, author, year, issue):
        super().__init__(name, author, year)
        self.issue = issue

    def __str__(self):
        return f"{super().__str__()} ,  Issue: {self.issue}"

book = Book("Book", "Author", 2000, 100)
print(book)
book.check_out()
print(book)
book.return_item()
print(book)

dvd = DVD("DVD", "Author", 2000, 120)
print(dvd)
dvd.check_out()
print(dvd)
dvd.return_item()
print(dvd)

magazine = Magazine("Magazine", "Author", 2000, 1)
print(magazine)
magazine.check_out()
print(magazine)
magazine.return_item()
print(magazine)
