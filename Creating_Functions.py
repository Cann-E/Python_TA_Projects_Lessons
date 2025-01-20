#Creating Funtcitons explanation
#Function Block of Reusable Code
#greet() after creating the function to call or invoke it!


def greet(name):#name is parameter to show it will accept the argument to print on line 6
    print("Hey There:")
    print("Welcome!",name)#to print the argument given when the function is called
    
# greet("Can") #Can is argument

def person(name,age,gender):
    name=(f"Your name is {name} ")
    age=(f"You are {age} years old!")
    gender=(f"You are {gender}!")
    

people=int(input("How Many People?: "))

for i in range(people):
    name=input("Whats Your name?: ")
    age=int(input("How old are you?: "))
    gender=input("Whats your gender?: ")
    print("Person Added!")

    
print(f"{people} Person Added To the list!")



#return = statement used to end a  function and send a result back to the caller

def sum(num1,num2):
    total=num1+num2 
    return total 

print(sum(5,7))


def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=create_name("Can","Ercan")
print(full_name)
