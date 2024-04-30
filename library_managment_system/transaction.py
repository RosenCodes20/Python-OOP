from book import Book
from member import Member


class Transaction:

    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.returned = False

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise ValueError("The value should be some book!!")

        self.__book = value

    @property
    def member(self):
        return self.__member

    @member.setter
    def member(self, value):
        if not isinstance(value, Member):
            raise ValueError("The member should be a member value!!")

        self.__member = value