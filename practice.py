# if statement
# elif statement
# else statement
# while loops
# for loops
# def functions
# rEturn functions

import random

# #1 IF FUNCTION

bar_age=int(input("Please Enter Age: "))

if bar_age>=18:
    print("Welcome to our Bar!")
    
#2 IF ELIF FUNCTION

restroom_gender=input("Please Pick your Gender for the Restrooms: ").lower()

if restroom_gender=="male":
    print("Please Go to MEN Restroom!")
elif restroom_gender=="female":
    print("Please Go to Women Restroom!")
    
# #3 IF ELIF ELSE FUNCTION 

price=float(input("Please Enter the cost of this Shirt: "))

if price>50 :
    print("This shirt cost",price,"and its expensive!")
elif price <=50:
    print("This shirt price is:",price,"its not expensive!")
else:
    print("Wrong Input_")
    
# #4 WHILE LOOPS

raffle=int(input("How many tries would you like to have!: "))

while raffle>0:
    roll_dice=random.randint(1,6)
    print("You roll the dice: ",roll_dice)
    raffle-=1
    if roll_dice==6 :
        print("Congrats You win!")
        break
        
print("Thank you for Entering the Raffle!")


#5 FOR LOOPS

sentence_=input("Please Enter Your Sentence: ")
for each_letter in sentence_:
    if each_letter==" ":
        continue
    print(each_letter)

   
for numbers in range(1,100):
    if numbers%2 == 0:
        print("Even",numbers)
    else:
        print("Odd",numbers)
        
    

#6 DEF FUNCTIONS

def person(name,age,gender):
    print("Your name is",name)
    print("Your age is",age)
    print("You are",gender)
    
person("Can",31,"Male")



def person(name,age,gender):
    print("Your name is",name)
    print("Your age is",age)
    print("You are",gender)
    
count=int(input("How Many People?: "))
total=0

while count>0:
    name=input("Whats your name: ")
    age=int(input("Whats Your age: "))
    gender=input("Whats your gender: ")
    count-=1
    print("Person Added!",name,gender)
    total+=1
    
print("Total person count",total)


#7 RETURN FUNCTIONS

def add(num1,num2):
    total=num1+num2
    return total

print(add(5,7))


#8 Creating Objects


        