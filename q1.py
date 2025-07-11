# This code defines a Book class with methods to mark a book as borrowed or returned.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True   

    def  mark_as_returned(self):
        self.is_borrowed = False  


# This code defines a Library Member class with methods to borrow, list borrowed books and return books.
class LibraryMember:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            print(f"{self.name} borrowed '{book.title}' by {book.author}.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book.is_borrowed:
            book.mark_as_returned()
            print(f"{self.name} returned '{book.title}'.") 
        else:
            print(f"'{book.title}' was not borrowed.")   

    def list_borrowed_books(self, books):
        print(f"{self.name}'s borrowed books:")
        borrowed = False
        for book in books:
            if book.is_borrowed:
                print(f"- {book.title} by {book.author}")
                borrowed = True
        if not borrowed:
            print("No books borrowed.")                       

# Create instances and demonstrate functionality
if __name__ == "__main__":
    # Example usage
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    member = LibraryMember("Tommy")

    member.borrow_book(book1)
    member.borrow_book(book2)
    member.list_borrowed_books([book1, book2])
    member.return_book(book1)
    member.list_borrowed_books([book1, book2])