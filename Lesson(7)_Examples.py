#1

accept_message=input("Please enter a message: ")

while accept_message != "done":
    print("We got your Message")
    accept_message=input("Please Enter another Message: ")
    
print("Thank you for your messages")



#2

password1=input("Please Create first password: ")
print("Thank you Your password has been created!")
password2=input("Please Create second password: ")
print("Thank you Your password has been created!")

login=input("Please Enter the password you created: ")

while login != password1 and login != password2:
    print("Invalid Password")
    login=input("Please Try Again: ")
    
print("Welcome Back!")




#3

num=0

while num <3 :   
    name=input("Please Enter your Name: ")
    print("Congrats",name,"You saved %20 percent!")
    num +=1
    
print ("All Done!")



# #4

language=input("Please Enter a Programming language: ").lower()
tries=1
count=5

while language != "python" and count>1:
    print("INVALID LANGUAGE")
    language=input("Please Try Again: ")
    tries +=1
    count -=1
    
print("It took you",tries,"total.")




#5

ticket=input("Please Enter Ticket Number: ")
if ticket=="0":
    new_ticket=0
    new_ticket=input("Please Enter New Ticket Number: ")
    while new_ticket != "1":
        print("Train Ticket number is",new_ticket)
        new_ticket=input("Please Enter New Ticket Number: ")
    print("Program Complete Thank you!")
else:
    print("Program Not Started Try Again")




#6

selection=input("Please choose 1 or 2: ")

if selection=="1":
    weather=input("Whats your ideal weather?: ").lower()
    if weather=="cold":
        print("Go ski holiday!")
    else:
        print("Go to beach!")
elif selection=="2":
    answer=input("Please guess correct answer: ")    
    if answer !="correct":
        raffle=4   
        while raffle>1:
            raffle -=1
            answer=input("Please try again: ")
        else:
            print("Sorry no more tries left!")      
    else:
        print("You get free trip!")
    
        
    
    
        

        
        