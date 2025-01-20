#1

watch_movie=input("Do you want to watch a movie?: ").capitalize()

if watch_movie=="Yes":
    genre=input("What genre do you want to watch?: ").lower()
    if genre=="comedy":
        print("Watch the Hangover Trilogy!!")
    else:
        print("Watch Top Gun!")
else:
    print("Watch a TV series!")
    
    
#2

choice=input("Do you want to stay at hotel or resort?: ").lower()
if choice=="resort":
    price=float(input("Whats the max price you want to spend per night?: "))
    if price>= 350:
        print("Book six senses resort!!")
    else:
        print("Book Four Seasons!!")
elif choice=="hotel":
    print("Book the nearest Hilton Hotel!!")

#3

price_1=float(input("Whats the price of your first product?: "))
price_2=float(input("Whats the price of your second product?: "))
price_3=float(input("Whats the price of your third product?: "))
total=price_1+price_2+ price_3

if price_3>price_2 and price_3>price_1:
    total=(price_3+ price_2+price_1)/2
    print("Half off!!")
elif price_1>price_2 and price_1>price_3:
    total=(price_3+ price_2+price_1)*0.34
    print("66% off!!")
print ("Your total is:",total)


#4

cost=float(input("Whats your cost?: "))
curr_time=float(input("What the current time in militray hour format?: "))

if curr_time>= 7 and curr_time<=9:
    discounted_price=cost*0.8
    print("New total is:",discounted_price)
elif curr_time>=10 and curr_time<=18:
    print("No discount your cost is:",cost)
else:
    print("We are closed!")


#5

review_score=int(input("Please Review us from (1-10): "))

if review_score>= 9:
    print("Thank you so much!")
if review_score<9 and review_score >=5:
    improve=input("How can we improve for you!!?: ")
    print(improve,"We will work harder!")
else:
    print("We are sorry to hear that!")
