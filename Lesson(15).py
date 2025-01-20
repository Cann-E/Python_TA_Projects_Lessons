#Super Class and Inheritance

class Animal():
    
    def __init__(self,type):
        self.type=type
        
class Dog(Animal):
    
    def __init__(self,type,color):
        super().__init__(type)
        self.property=color
    
    def dog_sound(self):
        print("WOOF WOOF")
        
        
        
class Agent():
    def __init__(self,name,health,weapon):
        self.name=name
        self.health=health
        self.weapon=weapon
        
    def player_info(self):
        print(f"Welcome {self.name}")
        print(f"Your Health is {self.health}")
        print(f"Your weapon is: {self.weapon}")
        
class Spy(Agent):
    def spy_talk(self):
        print(f"My name is {self.name} and my health is {self.health} and my weapon is {self.weapon}")
        
    def shoot(self,bad_guy):
        if bad_guy.health>0:
            bad_guy.health-=20
            
            print(f"{bad_guy.name} has lost 20 health. Remaining health: {bad_guy.health}")
        else:
            print(f"{bad_guy.name} is already down!")
            
jamesbond=Spy("James Bond",150,"M4")
ethanhunt=Agent("Ethan Hunt",100,"AK47")

ethanhunt.player_info()
jamesbond.spy_talk()

jamesbond.shoot(ethanhunt)


            
