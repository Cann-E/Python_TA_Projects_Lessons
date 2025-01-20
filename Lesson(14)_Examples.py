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
        
dog=Animals("Remy","dog","woof")
cat=Animals("Minnakh","cat","meow")

dog.pet_info()
dog.speak()

cat.pet_info()
cat.speak()


#2


class Player():
    def __init__(self,name,score):
        self.name=name
        self.score=score
        self.team=None
        
    def show_stats(self):
        print("Your Name is:",self.name)
        print("Your Player stats are:",self.score)
        print("Your Team is:",self.team)
        
    def select_team(self):
        self.team=input("Whats your team?: ")
        
        
player_1=Player("Lebron James",100)
player_2=Player("Kevin Durant",150)

player_1.select_team()
player_1.show_stats()

player_2.select_team()
player_2.show_stats()



#3


class Rectangle():
    def __init__(self,short_side,long_side):
        self.short_side=short_side
        self.long_side=long_side
        
    def rectangle_info(self):
        print("Rectangle have 4 side one is long one is short!")

        
    def rectangle_perimeter(self):        
        self.perimeter=(self.short_side+self.long_side)*2
        return self.perimeter
    
    def rectangle_area(self):
        self.area=(self.short_side*self.long_side)
        return self.area
    
    def shorten_lenght(self,long_side):        
        self.updated=(self.long_side-long_side)*self.short_side
        return self.updated
        

width=int(input("Please Enter Width: "))
lenght=int(input("Please Enter lenght: "))   

rectangle=Rectangle(width,lenght)

rectangle.rectangle_info()

print("Perimeter: ",rectangle.rectangle_perimeter())

print("Area: ",rectangle.rectangle_area())
        
reduction=int(input("How Much You want to Reduce the lenght: "))
print("Updated Area: ",rectangle.shorten_lenght(reduction))
        