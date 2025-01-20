#creating Objects
#constructor function __init__() initialize

# class Class_name():
#     def __init__(self,parameter):
#         self.property=parameter
#     def class_details(self):
#         print("Show me Details:",self.Property)
        
# object=Class_name(Argument)



class Agent():
    def __init__(self,name,health,car):
        self.name=name
        self.health=health
        self.car=car
    def player_info(self):
        print("WELCOME:",self.name)
        print("YOUR HEALTH IS:",self.health)
        print("YOUR CAR IS:",self.car)
        




spy=Agent("James Bond",100,"Jaguar")
villain=Agent("Ethan Hunt",45,"Ferrari")

spy.player_info()
villain.player_info()