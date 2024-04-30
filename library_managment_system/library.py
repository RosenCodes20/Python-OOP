from book import Book
from member import Member
from transaction import Transaction


class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, title, author, ISBN, copies):
        for book in self.books:
            if book.title == title:
                raise Exception("The book is already here!!")

        new_book = Book(title, author, ISBN, copies)
        self.books.append(new_book)
        return f"New book with title {title} written by {author} with ISBN number {ISBN} and {copies} copies!"

    def add_member(self, name, member_id):
        for member in self.members:
            if member.member_id == member_id:
                raise Exception("The member is already here!!")

        new_member = Member(name, member_id)
        self.members.append(new_member)
        return f"Added a new member with name {name} and member id: {member_id}!"

    def issue_book(self, title, name):
        try:
            book = next(filter(lambda b: b.title == title, self.books))

        except StopIteration:
            raise Exception(f"Book with title {title} cannot be found!!")

        try:
            member = next(filter(lambda m: m.name == name, self.members))

        except StopIteration:
            raise Exception(f"Member with name {name} cannot be found here!!")

        if book.copies > 0:
            new_transaction = Transaction(book, member)
            book.copies -= 1
            self.transactions.append(new_transaction)
            return f"Successfully added a new transaction!"

        else:
            return f"No book copies left here!!"

    def return_book(self, book: Book):
        try:
            transaction = next(filter(lambda t: t.book == book, self.transactions))

        except StopIteration:
            raise Exception("Cannot found the transaction in here!!")

        if not transaction.returned:
            transaction.returned = True
            transaction.book.copies += 1
            return f"Successfully returned the transaction"

        else:
            return f"The transaction is already returned!!"

    def list_books(self):
        result = "Here are the book details:\n"
        for book in self.books:
            result += f"Title: {book.title}\n" \
                   f"Author: {book.author}\n" \
                   f"ISBN: {book.ISBN}\n" \
                   f"Copies: {book.copies}"

        return result

    def list_members(self):
        result = "Here are the member details:\n"

        for member in self.members:
            result += f"Name: {member.name}\n" \
                      f"Member_id: {member.member_id}"

    def __repr__(self):
        member_details = [m.representing_member() for m in self.members]

        return "\n".join(map(str, member_details))