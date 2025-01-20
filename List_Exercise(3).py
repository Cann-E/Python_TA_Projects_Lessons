

movie_watchlist=list()

def add_movies():
    add_movie=input("Please Enter the movie name you want: ")
    movie_watchlist.append(add_movie)
    return add_movie

def remove_movies():
    print(f"{movie_watchlist} these movies are in your list\n")
    remove_movie=input("Please Enter the movie you want to delete from the list: ")
    if remove_movie not in movie_watchlist:
        print(f"{remove_movie} Error movie not in the list")
    else:
        movie_watchlist.remove(remove_movie)
        print(f"{remove_movie} remove from your list")
        return remove_movie
        
def view_watchlist():
    print(f"{movie_watchlist} these are your moves in your watchlist!")
    
    
def mark_watched():
    print(f"{movie_watchlist} these are your moves in your watchlist!")
    movie_watched=input("Please Enter Which movie you watched already: ")
    if movie_watched in movie_watchlist:
        movie_watchlist.remove(movie_watched)
        movie_watchlist.append(f"{movie_watched},(WATCHED)")
    else:
        print(f"{movie_watched} is not in your watchlist!")
        
        
        
        
while True:
    system_=input("Welcome to the Movie Watchlist Manager!\n"
                  "1-Add Movie \n"
                  "2-Remove Movie \n"
                  "3- View Watchlist \n"
                  "4- Mark Movie as Watched \n"
                  "5-Exit \n"
                  
                  ).lower()
    
    if system_ =="1":
        movie_add=add_movies()
        print(f"{movie_add} added to your watchlist\n")
        
    elif system_ =="2":
        remove_movies()
        
    elif system_ =="3":
        view_watchlist()
        
    elif system_=="4":
        mark_watched() 
        
    elif system_ =="5" :
        print("Program Terminated")
        break