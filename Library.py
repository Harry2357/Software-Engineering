class Library:
    def __init__(self, books, borrowers, loans):
        self.__books = books
        self.__borrowers = borrowers
        self.__loans = loans



    def display(self):
        print("Books:")
        for book in self.__books:
            book.display()
            print("")
        print("Borrowers:")
        for borrower in self.__borrowers:
            borrower.display()
            print("")
        print("Loans:")
        for loan in self.__loans:
            loan.display()
            print("")
    
    def getBooks(self):
        return self.__books
    def getBorrowers(self):
        return self.__borrowers
    def getLoans(self):
        return self.__loans
    

    def addLoan(self,loan):
        self.__loans.append(loan)

    def returnBook(self, bookID):
        for l in self.__loans:
            if l.getBookID() == bookID:
                #del l
                self.__loans.remove(l)
                print("Book Returned")
                return
        print("Book not found in loans")

    def getBookStatus(self, bookID):
        for l in self.__loans:
            if l.getBookID() == bookID:
                # "Books can be onLoan, available, or overDue"
                if l.overdue():
                    return "Overdue"
                else:
                    return "On loan"
        return "Book available"