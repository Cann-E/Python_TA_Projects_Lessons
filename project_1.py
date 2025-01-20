#AI 
#CanGPT

#STRUCTURE
# 1- INPUT STATEMENT TO START THE SYSTEM
# 2- MAIN WHILE LOOP(REPEAT AUNTIL AND EVENT)
# 3- CONDITIONAL STATEMENTS (IF/ELIF/ELSE)
# 4- PRINT()
# 5- TRY ADDING THE FOR LOOP
# 6- 5 OR MORE ACTIONS 
# 7- NESTING IS KEY !
# (MINIMUM 50 LINES)

import random

system_=input("Press 1 to start press 2 to end the system: ")


while system_=="1":    
    greet=input("Welcome User What would you like to do today!\n"
                "1-Watch a movie\n"
                "2-Go Outside\n"
                "3-Invite Friends for Drink\n"
                "4-Order Grocery Delivery\n"
                "5-I dont know\n"
                "6-Buy Shoes\n"
                "7-Buy Video Games\n"
                "8-Calculator\n"
                "9-Split My Sentence\n"
                "10-Happy New Year\n"
                "11-Recommend Me A Book\n"
                "12-Travel\n"
                ).lower()
    
    if greet in ("watch a movie","1"):
        response_1=input("What kinda movie would you like to watch:1-Horror 2-Action 3-Romance 4-Sci-Fi 5-Comedy  : ").lower()
        if response_1== "horror":
            print("Go watch Exorcism!")
            break
        elif response_1 == "action":
            print("Go watch Top Gun!")
            break
        elif response_1 == "romance":
            print ("Go Watch Notebook!")
            break
        elif response_1== "sci-fi":
            print("You can watch X-Files!")
            break
        elif response_1=="comedy":
            print("You can watch Hangover!")
            break
        
    elif greet =="go outside" or greet=="2":
        response_2=input("What kinda outside event would you like to do Dinner,Sports or Shopping?: ").lower()
        while response_2 == "dinner":
            response_3=input("What kinda food would you like to have?: ").lower()
            if response_3=="mexican food":
                print("You can Go to la Panza Feliz!")
                break
            elif response_3 =="asian":
                print("You can Go to Shogun's")
                break
        while response_2=="sports":
            response_4_temperature=int(input("Whats the temperature outside so i can recommaend you some sports activities?: "))
            if response_4_temperature <= 20 and response_4_temperature >=5 :
                print("Weather seems to be nice outside not too hot not to cold i would recommend playing soccer!")
                break
            elif response_4_temperature >= 30 :
                print("I wouldnt Recommend outside sports activities its too hot")
                break
            elif response_4_temperature <5 :
                print("Its too cold outside i would recommend a brisk walk with a jacket on!")
        while response_2 == "shopping":
            money=int(input("How much money do you have for shopping?: "))
            if money<=10 :
                print("You shouldnt go to shopping cause you poor my boi!")
                break
            elif money>10 and money<=50:
                print ("You should go to walmart cause your budget is less than 50 usd!")
                break
            else:
                print("Goddayum you rich sonuva!")
                break
            
    elif greet=="invite friends for drink" or greet=="3":
        guests=int(input("Please Enter Guest Number: "))
        for i in range(guests):
            name=input("Enter Guest Name: ").capitalize()
            lastname=input("Enter Guest Last Name: ").capitalize()
            age=int(input("Enter Guest Age: "))
            if age <18 :
                print("You shouldnt invite",name,lastname,"is too young",name,"is",age,"years old!!!!")
            else:
                print(name,lastname,"Added to guest list they can come to your party!")
                
    elif greet== "order grocery delivery" or greet=="4":
        response_5=input("What would you like to order from the store?: ").lower()
        if response_5=="apples":
            apple_quantity=int(input("Apple price is 1 usd How many apples would you like to order?: "))
            apple_price=1
            total_apple=apple_quantity*apple_price
            print("Total cost for apples is gonna be",total_apple,"usd")
        elif response_5 == "chicken" or response_5=="bread":
            if response_5 == "chicken":
                chicken_price=10
                print("Its gonna be",chicken_price,"usd for chicken")
            elif response_5 == "bread":
                bread_price= 5
                print("Its gonna be",bread_price,"usd for bread")
                
    elif greet=="i dont know" or greet=="5":
        play_dice=input("Would you like to play dice game with me?: ").lower()
        if play_dice=="yes":
            print("Okay Lets Roll the Dice 2 times lets see who wins first dice roll is yours and second is mine!!")
            chances=2
            while chances>0:
                roll_dice=random.randint(1,6)
                chances-=1
                print("The dice roll results are: ",roll_dice)
        elif play_dice=="no":
            print("Okay lets play word game lets find the invalid symbols in a sentence and count them!")
            word_create=input("Please Enter A sentence: ")
            invalid="!@#$%^&*()_+1234567890"
            for i in word_create:
                if i in invalid:
                    print(i,"These Are the invalid symbols!")
                    
    elif greet=="buy shoes" or greet=="6":
        shoe_count=int(input("How many Shoes would you like to buy?: "))
        def shoes(price,shoe_count):
            return price*shoe_count
        total_shoe_cost=shoes(100,shoe_count)
        print("Total Shoe price is gonna be",total_shoe_cost)
        
    elif greet=="buy video games" or greet=="7":
        video_game_count=0
        total_video_price=0
        video_game_count=int(input("How Many Game would you like to buy?: "))        
        while video_game_count>0:
            video_game_name=input("Whats the name of the game?: ")
            video_game_price=float(input("How much you want to spend on this game?: "))
            total_video_price+=video_game_price
            video_game_count-=1
            print(video_game_name,"added to your cart and price is:",video_game_price)
            
        print("Total spend for the games are",total_video_price)
     
    elif greet in ("calculator","8"):
        num1=float(input("Please Enter Your First Number: "))
        num2=float(input("Please Enter Your Second Number: "))
        
        while True:
            operator = input("What would you like to use (+, -, *, /): ")
            
            if operator == "+":
                print("You choose to add your total is:",num1+num2)
                break
            elif operator == "-":
                print("You choose to subtract your total is:",num1-num2)
                break
            elif operator == "*":
                print("You choose to multiply your total is:",num1*num2)
                break
            elif operator == "/":
                print("You choose to divide your total is:",num1/num2)
                break
            else:
                print("Invalid Operator Try again. ")
    
    elif greet in ("split my sentence","9"):
        sentence=input("Enter Your Sentence: ")
        for each_letter in sentence:
            print("Character :",each_letter)
    
    elif greet in ("happy new year","10") :
            for count in reversed(range(1,11)): 
                if count>0 :
                    print (count,"GET READY!") 
            print("BLAST OFF HAPPY NEW YEAR!!!!!!")
    
    elif greet in ("recommend me a book","11"):
        lenght_book=int(input("How long of a book are you looking for: "))
        while lenght_book>=100 and lenght_book<=300:
            book_era=input("What era you looking for to read: ").lower()
            if book_era=="victorian":
                print("You can read Oliver Twist.")
            elif book_era=="romantic":
                print("You can Read Pride And Prejudice")
            break
        while lenght_book<100 and lenght_book>1:
            kids_book=input("These are gonna be the kids book what kind of genre are you looking for: ").lower()
            if kids_book=="princess" or kids_book== "romantic":
                print("You can read Sleeping Beauty!")
            break
        while lenght_book>=500 and lenght_book<=2000:
            long_book_genre=input("You choose a very long book what kinda genre are you intrested in: ")
            if long_book_genre=="horror" or long_book_genre=="scary book":
                print("You can read Nosferatu")
            break
    
    elif greet in ("travel","12") :
        travel_=input("What kinda place would you like to travel: \n"
                    "1-Cold: \n"
                    "2-Hot: \n"
                    "3-Warm: \n"
                    ).lower()
        if travel_ in ("cold","1"):
            while True:                
                    travel_budget=float(input("Whats Your budget?: "))
                    if travel_budget<=100 and travel_budget>=1:
                        print("You too poor my Friend Stay in your house!!")
                    elif travel_budget>100 and travel_budget<=500:
                        print("You can Stay at Four Seasons Colorado!")
                    else:
                        print("You Too rich boi you can stay anywhere you want maybe Ritz Colorado!")
                    
        if travel_ in ("hot","2"):#maybe fix!
            while True:
                travel_weather=int(input("How hot your thinking?: "))
                for temperature in range(20,30):
                    if travel_weather==temperature:
                        print("Thats not that hot you can Stay at Disney Florida!")
                        break
                for temperature in range(31,40):
                    if travel_weather==temperature:
                        print("Thats quite hot you can stay at Texas Galleria Hotel!")
                        break
                for temperature in range(41,60):
                    travel_weather==temperature
                    print("Thats Scorching hot you should stay at Sahara Desert Hotel!")
                    break
                
        if travel_ in ("warm","3"):#fix not finished yet!
            while True:
                travel_days=int(input("How many days would you like to stay?: "))
                for days in range(1,3):
                    travel_days==days
                    print("You should go somewhere close to you cause 1-3 days is not that long of vacation so I would recommend Downtown Austin")
                    break
                for days in range(4,7):
                    travel_days==days
                    print("That is a good amount of Time\n"
                          "You Should Consider Going to New York"
                          )
                    break
                for days in range(8,14):
                    travel_days==days
                    print("Thats Quite Long Time You should fly international:\n"
                          "Like London or Paris"
                          )
                    break
                        
                    
                
            
                              
                
    
    
    
    system_ = input("Press 1 to continue or 2 to terminate the system: ")                
            
            
            
if system_ =="2":
    print("Program Terminated!!")
    


            
                
                
                
            
            
    