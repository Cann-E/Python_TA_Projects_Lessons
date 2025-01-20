#libraryr Management Systems

class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.status="available"
        
    def check_out(self):
        if self.status=="checked out":
            print(self.title,"The Book is already Checked out Sorry!")
        else:
            self.status=="checked out"
            print("The book is available to check out: ",self.title)
    
    def return_book(self):
        if self.status=="checked out":
            self.status=="available"
            print(self.title,"The book Has been returned!")
        elif self.status=="available":
            print("The book is already in the system!")
            
            

class Library():
    def __init__(self):
        self.books=[]
        
    def add_books(self,book):
        self.books.append(book)
        
    def view_books(self):
        for book in  (self.books):
            print(f"{book.title} by {book.author} and the status is: {book.status}")
        
    def search_books(self,title):
        for book in  (self.books):
            if book.title.lower() == title.lower():
                print(f"Found: Title: {book.title}, Author: {book.author}, Status: {book.status}")
                return
            else:
                print("Book not found!")
                
             
        
        
        
        
        
        
        
    

library=Library()
system_=input("Welcome to the library Manament System!\n"
                  "\n"
                  "1-Add a new book\n"
                  "2-View all books\n"
                  "3-Search for a book\n"
                  "4-Check out a book\n"
                  "5-Return a book\n"
                  "6-Quit\n"
                  "\n"
                  "Enter Your Choice: "
                  ).lower()

while True:
    if system_ == "1" or system_ == "add a new book":
        print("You choose to add a new book to the system!\n")
        add_book_name=input("Whats the book's name you want to add?: ")
        add_book_author=input("Whats the author of the book you want to add?: ")
        book=Book(add_book_name,add_book_author)
        library.add_books(book)
        print(f"{add_book_name} by {add_book_author} is added to the system!")
        
    elif system_ =="2" or system_ == "view all books":
        print("You choose to view all the books!")
        