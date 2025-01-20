

class Library():
    def __init__(self):
        self.books=[]
    
    
    def add_book(self):
       book_add=input("Whats the tile of the book you want to add: ")
       self.books.append(book_add)
       return book_add
       
    def remove_book(self):
        print(f"{self.books} these are all the books in the library!")
        book_remove=input("Which book would you like to remove: ")
        if book_remove in self.books:
            self.books.remove(book_remove)
            return book_remove
        else:
            print(f"{self.books} is not in the library system!")
            
    def view_books(self):
        print(f"{self.books} these are all the books in the library!")
        
    def search_book(self):
        book_search=input("What the title of the book you searching: ")
        if book_search in self.books:
            print(f"{book_search} is in the library system!")
        else:
            print("Search failed book not found!")            
    
can_library=Library()  
    
while True:
        system_=input("Welcome to the Cans Library!\n"
                  "1-Add Book \n"
                  "2-Remove Book \n"
                  "3- View all Books \n"
                  "4- Search for a book \n"
                  "5-Exit \n"
                  
                  ).lower()
        
        if system_=="1":
            add=can_library.add_book()
            print(f"{add} is added to the library system!\n")
            
        elif system_ =="2":
            remove=can_library.remove_book()
            print(f"{remove} is removed from the library system!\n")
            
        elif system_ == "3":
            can_library.view_books()
            
        elif system_=="4":
            search=can_library.search_book()
            
        elif system_=="5":
            print("Program Terminated\n")
            print("Thank you for visiting Can Library!")