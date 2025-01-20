#For Loops  in()  range()

name=input("Please Enter Your First Name and Last Name: ")
invalid="1234567890"

for letter in name:
    if letter in invalid:
        print("This Character is invalid!!",letter)
        
        
        
        
        
passengers=int(input("Please Enter How Many Passengers?: "))

for i in range(passengers):
    firstname=input("Please Enter First Name: ")
    lastname=input("Please Enter Last Name: ")
    print("Hello",firstname,lastname)
print("Passengers Updated!")
    
        