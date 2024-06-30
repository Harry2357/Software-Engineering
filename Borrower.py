borrowerIdCounter = 0 # different name to global variable 'idCounter' can't have same globals in 1 folder (cant import)
class Borrower:
    def __init__(self, name, role):
        global borrowerIdCounter
        self.__name = name
        self.__id = borrowerIdCounter
        borrowerIdCounter += 1
        self.setRole(role)

    def setRole(self, role):
        if role in ['staff', 'student', 'parent']:
            self.__role = role
        else:
            print("Error; Invalid role.")
            self.__role = 'unkown'
    
    def display(self):
        print(f"Name: {self.__name}")
        print(f"Role: {self.__role}")
        print(f"ID: {self.__id}")

    def getName(self):
        return self.__name
    def getID(self):
        return self.__id
    def getRole(self):
        return self.__role
       

# TEST
if __name__ == '__main__': # if this is our main file (the one you run), do this:
    myBorrower = Borrower('Harry', 'student')
    myBorrower.display()