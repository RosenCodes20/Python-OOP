class Book:

    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Please enter some title!!")
        
        self.__title = value
        
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Please enter an author")
        
        self.__author = value
        
    @property
    def ISBN(self):
        return self.__ISBN
    
    @ISBN.setter
    def ISBN(self, value):
        if not len(value) == 10 or not len(value) == 13:
            raise ValueError("The ISBN should be 10 or 13 symbols")
        
        self.__ISBN = value
        
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def copies(self, value):
        if value < 0:
            raise ValueError("Copies can't be a negative number!!")

        self.__copies = value