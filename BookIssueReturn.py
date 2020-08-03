from Catalog import Catalog

class BookissuedReturn:
    
    def issuedBook(name, student_id, book_name,):
        for book in Catalog.books_list:
            if book.name == book_name and len(book.book_name) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                Catalog.updateIssuerInfo(book_item, name, student_id,)
                Catalog.addToissuedList(book_item)
                return book_item
        else:
            print("This book is not available.")
    
    def returnBook(ret_book_item,):
        for book in Catalog.books_list:
            if book == ret_book_item.book:
                book.book_item.append(ret_book_item)
                book.total_count += 1
        Catalog.clearIssuerInfo(ret_book_item)
        Catalog.removeFromissuedList(ret_book_item)