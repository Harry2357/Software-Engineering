from Book import Book
from Borrower import Borrower
from Loan import Loan
from Library import Library
import datetime
# create some books 
books = []
books.append(Book(title="Philosopher's Stone", author="J.K. Rowling", category="fiction"))
books.append(Book(title="Charlotte's Web", author="E.B. White", category="fiction"))
books.append(Book(title="The Lion, the Witch and the Wardrobe", author="C.S. Lewis", category="fiction"))
books.append(Book(title="Matilda", author="Roald Dahl", category="fiction"))
books.append(Book(title="Harry Potter and the Chamber of Secrets", author="J.K. Rowling", category="fiction"))
books.append(Book(title="Percy Jackson & the Olympians: The Lightning Thief", author="Rick Riordan", category="fiction"))
books.append(Book(title="Anne of Green Gables", author="L.M. Montgomery", category="fiction"))
books.append(Book(title="The Secret Garden", author="Frances Hodgson Burnett", category="fiction"))
books.append(Book(title="A Wrinkle in Time", author="Madeleine L'Engle", category="fiction"))
books.append(Book(title="Winnie-the-Pooh", author="A.A. Milne", category="fiction"))
books.append(Book(title="The Tale of Peter Rabbit", author="Beatrix Potter", category="fiction"))
books.append(Book(title="Charlie and the Chocolate Factory", author="Roald Dahl", category="fiction"))


# create some borrowers
borrowers = []
borrowers.append(Borrower(name="Alice", role="student"))
borrowers.append(Borrower(name="Bob", role="staff"))
borrowers.append(Borrower(name="Charlie", role="parent"))
borrowers.append(Borrower(name="Daisy", role="student"))
borrowers.append(Borrower(name="Edward", role="staff"))
borrowers.append(Borrower(name="Fiona", role="parent"))
borrowers.append(Borrower(name="George", role="student"))
borrowers.append(Borrower(name="Hannah", role="staff"))
borrowers.append(Borrower(name="Ian", role="parent"))
borrowers.append(Borrower(name="Jane", role="student"))
borrowers.append(Borrower(name="Kevin", role="staff"))
borrowers.append(Borrower(name="Luna", role="parent"))

# create some loans:
loans = []
loans.append(Loan(books[0].getID(), borrowers[0].getID(), datetime.datetime(2021, 12, 25)))
loans.append(Loan(books[1].getID(), borrowers[3].getID(), datetime.datetime(2021, 12, 25)))
loans.append(Loan(books[2].getID(), borrowers[2].getID(), datetime.datetime(2021, 12, 25)))
loans.append(Loan(books[3].getID(), borrowers[1].getID(), datetime.datetime(2021, 12, 25)))

# add the data into a library
library = Library(books, borrowers, loans)

# get status of book id 1:
print("Book 1 status", library.getBookStatus(1))
library.returnBook(1)
print("Book 1 status", library.getBookStatus(1))

#for i in loans:
#    i.display()