from BookReserveReturn import BookissuedReturn
from Catalog import Catalog


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
    def viewBooks(self):
        Catalog.displayAllBooks()
        
class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self, name, author, publish_date, pages):
        Catalog.addBook(name, author, publish_date, pages)
        
    def addBookItem(self, name, isbn, rack):
        Catalog.addBookItem(name, isbn, rack)
    
    def removeBook(self, rem_book):
        Catalog.removeBook(rem_book)
        
    def removeBookItem(self, rem_bookitem):
        Catalog.removeBookItem(rem_bookitem)
        
    def addMember(self, name, location, age, aadhar_id, student_id):
        Member(name, location, age, aadhar_id, student_id)
    
    def removeMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("{} is removed from the library".format(name))
                break
        else:
            print("No one found by searched name")
            
    def viewMembers(self):
        for member in Member.members_list:
            print(member)
        
    def searchMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                print(member)
                for book_item in member.issued_books_list:
                    print(book_item.book.title, book_item.isbn)
                break
        else:
            print("There is no any member in library by searched name.")
            
    def viewissuedBookItems(self):
        Catalog.viewissuedBookItems()
        
    def viewIssuerInfo(self):
        isbn = input("Please enter isbn of the book")
        Catalog.viewIssuerInfo(isbn)
    
class Member(User):
    members_list = []
    
    def addMemberList(cls, member):
        cls.members_list.append(member)
    
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_books_list = []
        Member.addMemberList(self)
        print("Member added".format(name))
        
    def __repr__(self):
        return self.name + " " + self.location + " " + self.student_id
        
    def searchByname(self, name):
        Catalog.searchByname(name)
    
    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)
    
    def searchByPublishDate(self, publish_date):
        Catalog.searchByPublishDate(publish_date)
        
    def searchBypages(self, pages):
        Catalog.searchBypages(pages)
        
    def returnBook(self):
        print("This book is with you: ")
        for book_item in self.issued_books_list:
            print(book_item.book.name, book_item.isbn)
        isbn = input("Enter isbn of returning book: ")
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                ret_book_item = book_item
            else:
                print("The book you are requesting to return is not with you!")
        BookissuedReturn.returnBook(ret_book_item,)
        self.issued_books_list.remove(ret_book_item)