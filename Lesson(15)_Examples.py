#Super Class and Inheritance

#1
class Animals():
    def __init__(self,name,pet,sound):
        self.name=name
        self.pet=pet
        self.sound=sound
        
    def speak(self):
        print("Your Animal sound is :",self.sound)
        
    def pet_info(self):
        print("Your pet name is:",self.name)
        print("Your this pet:",self.pet)
        
        
class Fish(Animals):
    
    def swim(self):
        if self.sound =="None":
            print("I am a fish,I do not have a sound!")
        else:
            print("Are you sure you are a fish?")
            
    def ocean(self):
        self.response_1=input("Which ocean are your from?: ")
        print(f" {self.name} is a {self.pet} who lives in {self.response_1}")
        
        
        
        


# fish_1=Fish("Nemo","Fish","None")

# fish_1.speak()
# fish_1.pet_info()

# fish_1.swim()
# fish_1.ocean()
        


#2

class Vehicles():
    
    def __init__ (self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
              
    def car_info(self):
        if self.make=="ford" or self.make== "chevy"   or self.make=="tesla":
             return "American Make"
        
        else:
            
            return "Imported"   
              
    def vehicle_model(self):
        print(f"Your car Model is {self.make}")   
        
    def age_(self):
        if self.year>2000:
            print("Car from 21st century")      
        else:
            print("This car is old!")
            
    def price_(self,max_price):
        self.max_price=max_price
        if self.price<self.max_price:
            print("Within your budget!")
        else:
            print("Over Budget")        
            
            
class Style(Vehicles):
    
    def __init__(self, make, model, year, price,num_of_doors):
        super().__init__(make, model, year, price)
        self.num_of_doors=num_of_doors  
    
    def door_number(self):
        if self.num_of_doors==4 :
            print("Family Car!")
        else:
            print("Sports Car")
            
            
    
                       
             
 
 
 
 
 
 
 
             
              
ford_mustang = Vehicles("ford","Mustang",2021,25000)
print(ford_mustang.car_info())
ford_mustang.price_(24000)

maserati_ghibli=Style("maserati","Ghibli",2017,31000,4)
print(maserati_ghibli.car_info())
maserati_ghibli.vehicle_model()
maserati_ghibli.door_number()

chevy_corvette=Style("chevy","Corvette",1993,13500,2)
print(chevy_corvette.car_info())
chevy_corvette.age_()
chevy_corvette.door_number()


