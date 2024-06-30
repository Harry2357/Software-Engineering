idCounter = 0
class Book: 
    def __init__(self, author, title, category):
        global idCounter  # Global must be inside fn "Use the global variable"
        self.__author = author
        self.__title = title
        self.__id = idCounter
        idCounter += 1
        self.setCategory(category)
    
    # Verify that the category is 'valid' (Data Validation)
    def setCategory(self, category):
        # non-fiction, fiction, reference
        category = category.lower()
        if category in ['non-fiction', 'fiction', 'reference']:
            self.__category = category
        else:
            print("Error, Unknown category")
            self.__category = 'unknown'

    # Display book info
    def display(self):
        # title, author, id, category
        #print("Author: {} Title: {}".format(author, name))
        print(f"Title:{self.__title}, Author: {self.__author}, Category: {self.__category}, id: {self.__id}")

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.___title
    
    def getAuthor(self):
        return self.__author


# TEST
if __name__ == "__main__":
    new_novel = Book(title="Philosopher's Stone", author="J.K. Rowling",category="fiction")
    new_novel.display()