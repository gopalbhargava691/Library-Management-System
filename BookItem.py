class BookItem:
    issued_book_items = []
    
    def addissuedBooks(cls, book):
        cls.issued_book_items.append(book)
    
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        
    def updateIssuerInfo(self, name, student_id):
        self.info["Name"] = name
        self.info["Student ID"] = student_id
        
    def addToissueddList(self):
        BookItem.addissuedBooks(self)
        
    def removeFromissuedList(self):
        BookItem.issued_book_items.remove(self)
        
    def clearIssuerInfo(self):
        self.info.clear()