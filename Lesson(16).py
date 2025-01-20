#Lists  ages.append(age)  it means add input age to the list of ages    -- ages.sort()    sorting the list of ages A-Z OR 1-1000

ages=[10,15,25,35,74,82,11] # or list() function

print(ages[0]) #starting posiution first age!!!!

print(ages[-1]) #shows last element of the list!!!




ages=[3,7,54,2,21,45]

age=int(input("Please Enter an Age?: "))

while age!=0:
    if age in ages:
        print("You already entered that age!")
        
    else:
        ages.append(age)
    age=int(input("Enter an age: "))
        
ages.sort()
print(f"List of ages in your list: {ages}")



#if age in ages
#ages.append(age)
# #ages.sort()



ages=list()
age=int(input("Enter an age: "))
minors=0
seniors=0

while age !=0:
    ages.append(age)
    for age in ages:
        if age>70:
            seniors+=1
        elif age<18:
            minors+=1
        
    age=int(input("Enter a age: "))
    
print(f"All the ages {ages}")
print(f"NUmber of Minors are {minors} and number of seniros are {seniors}")








    
#.split(" ")
 
 
name="Can Ercan"
name=name.split(" ")

print("List of letters: ",name)