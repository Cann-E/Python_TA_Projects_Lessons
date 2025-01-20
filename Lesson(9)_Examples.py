#1

def total_points(game_score):
    points=0
    while game_score!=0:
        if game_score>=50 and game_score<=100:
            points+=2
        if game_score>100 and game_score <=200:
            points+=3        
        game_score=int(input("Enter the game Score: "))
    return points
            
score=int(input("Whats your Score: "))
game_points=total_points(score)
print("Total poins is:",game_points)


#2

def game_price(price):
    total=0
    
    while price !=0:
        
        
        if price>=69.99:
            print(game_name,"This Is a Triple A Game and its Expensive!!!")
            total+=price
            break
            
        elif price <69.99 and price>=49.99:
            print(game_name,"This is a Double A game and its Fairly Expensive!!")
            total+=price
            break
            
        elif price <49.99 and price >=29.99:
            print(game_name,"This Is a Single A game is And Price is OK!")
            total+=price
            break
            
        elif price <29.99 and price >=9.99:
            print(game_name,"This Is A indie Game and Price is Cheap")
            total+=price
            break
        
        
    return total
            
game_name=input("Enter Game Name: ")
price=float(input("Whats The Cost of the Game: "))
game_cost=game_price(price)
print("Total Cost is:",game_cost)