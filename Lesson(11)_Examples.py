
import random
# Create a mini lottery program
# Assign a variable a winning number and another variable a random number
# Show the random number with print
# if the winning number is equal to the random number, print "You win a free trip!"
# Otherwise, "Sorry, you didn't win..."


winning_number=15
random_number=random.randint(1,20)
print("Random Number is:",random_number)


if random_number!=winning_number:
    print("Sorry, you didn't win...")
else:
    print("You win a free trip!")


#################################################
# Create a program that assigns passengers to two different flights
# Ask the user if they want a new flight, if their answer is not "no" the program continues
# Create a variable for a random flight number
# if that random flight is equal to 1, increase a counter by 1
# if that random flight number is equal to 2, increase another counter by 1
# at the end of the loop, print off the number of passengers on both flights


flight_1=0
flight_2=0

response_1=input("DO you want to assign a new passenger to a flight?:(yes/no): ").lower()

while response_1!="no":
    
    passengers=random.randint(1,2)
    if passengers==1:        
        print("Assigned to Flight-1")
        flight_1+=1
    elif passengers==2:
        print("Assigned to Flight-2")
        flight_2+=1
    response_1=input("DO you want to assign a new passenger to a flight?:(yes/no): ").lower()
        
print("Flight 1 total passengers are:",flight_1)
print("Flight 2 total passengers are:",flight_2)



#################################################

# Create a guessing game. Create two variables, one with a random number, the other with an input
# if the input is too low, print "Too low, Try again."
# if the input is too high, print "Too high, try again."
# otherwise, print "Congrats! You got it!"



random_x=random.randint(1,10)
random_y=int(input("Please Enter A Random Number(1-10): "))

while random_y!=random_x:
    if random_y<random_x:
        print("Too low, Try again.")
    elif random_y>random_x:
        print("Too high, try again.")
    random_y=int(input("Please Enter A Random Number(1-10): "))   
    
print(random_y,"You got it correct!")





####################################
# Refactor your last guessing game to improve it
# We want to add the ability to continue guessing until we get the right number
# Think loops!
# Once the random number is guessed, print "Congrats" and the number of guesses it took the user

random_x=random.randint(1,10)
random_y=int(input("Please Enter A Random Number(1-10): "))
tries=0
while random_y!=random_x:
    tries+=1
    if random_y<random_x:
        print("Too low, Try again.")
    elif random_y>random_x:
        print("Too high, try again.")
    random_y=int(input("Please Enter A Random Number(1-10): "))   

print(tries,"total tries!")    
print(random_y,"You got it correct!")

