#1

def grade_(score):
    if score >=0 and score <50:
        print("Below passing,Improve Your grade!")
    elif score >=50 and score <70:
        print("Barely passing,Improve your Grade!")
    elif score>=70 and score<90:
        print("You have a passing grade!")
    else:
        print("Your one of the best in class!")
        
grade_score=int(input("Please Enter Your Exam Score: "))
print(grade_(grade_score))



#2

base_fare=100
print("Thank you for purchasing Plane Ticket!")

def extra_flight_charges(fare):
    upgrade=input("Would you like to upgrade(YES/NO): ").lower()
    
    if upgrade=="yes":
        fare+=99
        print("Ticket Upgraded!")
        
    baggage=input("Do you want to add baggage to your fare(YES/NO): ").lower()
    
    if baggage=="yes":
        fare+=35
        print("Baggage Added!")
    fare+=fare*0.08
    return fare   

total_fare=extra_flight_charges(base_fare)
print("Grand Total is:",total_fare)    




#3

def bank_balance(balance):
    if balance >=500:
        return True
    else:
        return False
    
bank_customer=int(input("How Many customers: "))

while bank_customer>0:
    name=input("Please Enter First Name: ")
    curr_balance=float(input("Please Enter Current Balance: "))
    bank_customer-=1
    if bank_balance(curr_balance):
        print("Your Balance is:",curr_balance,"No need to worry!",name)
    elif bank_balance!=curr_balance:
        print("Your Balance is:",curr_balance,"Your Account is low!",name)




#4

def mortgage(number):
    
    if number>=50:
        print("Instant Approvel!")
    elif number >=20 and number<50:
        print("You need approvel!")
    else:
        print("Not Approved!")
    return number


total_balance=0
        
while True:
    deposit=int(input("Please Enter Your Deposit(0 to terminate): "))
    if deposit==0:
        break
    total_balance+=deposit
    mortgage(deposit)
    
    
print("Total:",total_balance)

    
    
        