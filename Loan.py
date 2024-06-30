from datetime import datetime
loanIDCounter = 0
class Loan:
    def __init__(self, bookID, borrowerID, dueDate):
        global loanIDCounter   

        self.__bookID = bookID
        self.__borrowerID = borrowerID
        self.__dueDate = dueDate

        self.__ID = loanIDCounter
        loanIDCounter += 1

    def overdue(self):
        return self.__dueDate > datetime.now()
    
    
    def display(self):
        print(f"Loan ID: {self.__ID}") # <-- Added
        print(f"Book ID: {self.__bookID}")
        print(f"Borrower ID: {self.__borrowerID}")
        print(f"Due Date: {self.__dueDate}")
    
    # getters
    def getID(self):
        return self.__bookID
    
    def getBookID(self):
        return self.__bookID

    def getBorrowerID(self):
        return self.__borrowerID
    
    