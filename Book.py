from BookItem import BookItem

class Book:
        
    def __init__(self, name, author, publish_date, pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count +=1
        
    def printBook(self):
        print (self.name, self.author)
        for book_item in self.book_item:
            print (book_item.isbn)
            
    def viewissuedBookItems():
        if len(BookItem.issued_book_items) >= 1:
            for item in BookItem.issued_book_items:
                print(item.isbn)
        else:
            print("No books are issued at the moment!")
            
    def viewIssuerInfo(isbn):
        for book_item in BookItem.issued_book_items:
            if book_item.isbn == isbn:
                print("Issued by: " + book_item.info["Name"])
                print("Student ID: " + book_item.info["Student ID"])
                                
    def updateIssuerInfo(book_item, name, student_id):
        BookItem.updateIssuerInfo(book_item, name, student_id)
        
    def addToissuedList(book_item):   
        BookItem.addToissuedList(book_item)
        
    def clearIssuerInfo(ret_book_item):
        BookItem.clearIssuerInfo(ret_book_item)
        
    def removeFromissuedList(ret_book_item):
        BookItem.removeFromissuedList(ret_book_item)