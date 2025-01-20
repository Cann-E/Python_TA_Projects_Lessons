#Creating Functions!

#ex1

def person_info(name,age,sex):
    print("Your name is:",name)
    print("Your age is:",age)
    print("Your Gender is:",sex)
    


applicants=int(input("How many applicants are there: "))
for i in range(applicants):
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    sex=input("Enter Gender: ")
    person_info(name,age,sex)
    
    
    
# #ex2  

def car_brand(brand,model,year,title,miles,price):
    print("Car brand is:",brand)
    print("Car model is:",model)
    print("Car year is:",year)
    print("Car title is:",title)
    print("Car miles is:",miles)
    print("Car price is:",price)
    
car_count=int(input("How Many Cars Would you like to add to inventory: "))
car_inventory=0
car_inventory+=car_count

for i in range(car_count):
    brand=input("Whats the Brand of the Car: ")
    model=input("Whats the Model of this Car: ")
    year=int(input("Whats the year of this Car: "))
    title=input("Is the title Clean or Salvage: ")
    miles=float(input("Whats the mileage of this Car: "))
    price=float(input("Whats The asking Price of this Car: "))
    print("Car Added!!")
    car_brand(brand,model,year,title,miles,price)
    
print("Total Inventory is:",car_inventory)


#3

def people_(name,age,height,weight,gender):
    print("Your name is:",name)
    print("Your age is: ",age)
    print("You are",height,"inches tall")
    print("You weight",weight)
    print("Your gender is:",gender)
    
people_count=int(input("How Many People: "))

for i in range(people_count):
    name=input("Please Enter The Name: ")
    age=input("Please Enter The age: ")
    height=input("Please Enter The height: ")
    weight=input("Please Enter The weight: ")
    gender=input("Please Enter The gender: ")
    print("Person Added")
    people_(name,age,height,weight,gender) 

    
#return operator


def multiply(num1,num2):
    return num1*num2

print(multiply(6,8))
