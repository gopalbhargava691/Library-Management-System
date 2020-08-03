from Book import Book

class Catalog:
    def __init__(self):
      self.different_book_count = 0
      self.books = []

    #Only available to admin    
    def addBook(self, name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.addBooksList(b)
        Catalog.different_book_count += 1
        print("Book {} added successfully".format(name))
 
    #Only available to admin    
    def addBookItem(name, isbn, rack):
        for book in Catalog.books_list:
            if book.name == name:
                b = Book.addBookItem(book, isbn, rack)
                print("Book Item {} added successfully".format(isbn))
        
    def removeBook(rem_book):
        for book in Catalog.books_list:
            if book.name == rem_book:
                Catalog.books_list.remove(book)
                Catalog.different_book_count -= 1
                print("Book {} removed from the catalog".format(rem_book))
                
    def removeBookItem(rem_bookitem):
        for book in Catalog.books_list:
            for book_item in book.book_item:
                if book_item.isbn == rem_bookitem:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book Item {} removed from the catalog".format(rem_bookitem))
        
    def searchByname(name):
        for book in Catalog.books_list:
            if book.name == name:
                print("Book available")
                break
        else:
            print("No book is available by searched name")
    
    def searchByAuthor(author):
        count = 0
        for book in Catalog.books_list:
            if book.author == author:
                print(book.name)
                count += 1
        if count == 0:
            print("No books is available by searched author")
            
    def searchBypublishDate(publish_date):
        count = 0
        for book in Catalog.books_list:
            if book.publish_date == publish_date:
                print(book.name)
                count += 1
        if count == 0:
            print("No book is available by searched publish date")
            
    def searchBypages(pages):
         count = 0
         for book in Catalog.books_list:
             if book.pages == pages:
                 print(book.pages)
                 count += 1
         if count == 0:
             print("No book is available by searched pages")
            
    def displayAllBooks():
        c = 0
        for book in Catalog.books_list:
            c += book.total_count
            book.printBook()
        print("Different Book Count", Catalog.different_book_count)
        print("Total Book Count", c)
        
    def updateIssuerInfo(book_item, name, student_id):
        Book.updateIssuerInfo(book_item, name, student_id)
        
    def addToissuedList(book_item):   
        Book.addToissuedList(book_item)
        
    def clearIssuerInfo(ret_book_item):
        Book.clearIssuerInfo(ret_book_item)
        
    def removeFromissuedList(ret_book_item):
        Book.removeFromissuedList(ret_book_item)
        
    def viewissuedBookItems():
        Book.viewReservedBookItems()
        
    def viewIssuerInfo(isbn):
        Book.viewIssuerInfo(isbn)