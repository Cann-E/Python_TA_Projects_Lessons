from time import *


class Agents():
    def __init__(self,name,health,car):
        self.name=name
        self.health=health
        self.car=car
        
    def agent_information(self):
        print(f"Agent name is: {self.name} and Hp is : {self.health} \n"
              f"Agent Car is: {self.car}"
              )
        
class Spy(Agents):
    def __init__(self, name, health, car,agency,location,killed=False):
        super().__init__(name, health, car)
        self.agency=agency
        self.location=location
        self.killed=killed
        

        
    def attack_(self,spy):
        print(f"{self.name} Attacked! {spy.name}")
        if spy.health>0:
            
            spy.health-=20
            print(f"{spy.name} has lost 20 hp and current hp is {spy.health} left")
            
        elif spy.health<=0:
            spy.killed=True
            print(f"{spy.name} is dead now...")
            
            
            
tolga_elvermez=Spy("Tolga Elvermez",100,"Toyota Corolla","kaldirim UNV","MimarOba")
can_ercan=Spy("Can",105,"Maserati Ghibli","UH","Houston")

can_ercan.agent_information()

tolga_elvermez.agent_information()
sleep(5)

while tolga_elvermez.health>0:
    can_ercan.attack_(tolga_elvermez)
    sleep(2)
    if tolga_elvermez.health<=0:
        print("Tolga Elvermez started cryin and died.")
        break
    tolga_elvermez.attack_(can_ercan)
    sleep(2)
    

    
 


