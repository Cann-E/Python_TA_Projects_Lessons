

import random


rps=input("Please Choose your Hand(Rock/Paper/Scissors): ").lower()

robot_response=random.choice(["rock","paper","scissors"])

print("You chose:",rps)
print("AI chose:",robot_response)


while rps !=robot_response:
    if rps=="rock" and robot_response=="scissors":
        print("Rock beats Scissors!")
    elif rps=="rock" and robot_response=="paper":
        print("Paper beats Rock!!")
    if rps=="paper" and robot_response=="rock":
        print("Paper beats Rock!")
    elif rps=="paper" and robot_response=="scissors":
        print("Scissors beats Paper!!")
    if rps=="scissors" and robot_response=="rock":
        print("Rock beats Scissors!")
    elif rps=="scissors" and robot_response=="paper":
        print("Paper beats Rock!!")
    rps=input("Please Choose your Hand(Rock/Paper/Scissors): ").lower()
    
    
print("Draw TRY again: ")




#BETTER VERSION






rps = input("Please Choose your Hand (Rock/Paper/Scissors): ").lower()
robot_response = random.choice(["rock", "paper", "scissors"])

while True:
    print("You chose:", rps)
    print("AI chose:", robot_response)

    if rps == robot_response:
        print("Draw! TRY again:")
    elif rps == "rock" and robot_response == "scissors":
        print("Rock beats Scissors! You win!")
        break
    elif rps == "rock" and robot_response == "paper":
        print("Paper beats Rock! AI wins!")
    elif rps == "paper" and robot_response == "rock":
        print("Paper beats Rock! You win!")
        break
    elif rps == "paper" and robot_response == "scissors":
        print("Scissors beats Paper! AI wins!")
    elif rps == "scissors" and robot_response == "paper":
        print("Scissors beats Paper! You win!")
        break
    elif rps == "scissors" and robot_response == "rock":
        print("Rock beats Scissors! AI wins!")
    else:
        print("Invalid input! Please choose Rock, Paper, or Scissors.")

    rps = input("Please Choose your Hand (Rock/Paper/Scissors): ").lower()
    robot_response = random.choice(["rock", "paper", "scissors"])


    
    
    
