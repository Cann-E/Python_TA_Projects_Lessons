
class SmartHome():
    def __init__(self,thermostat=72,front_camera="Inactive"):
        self.living_room_light="OFF"
        self.bedroom_light="OFF"
        self.thermostat=thermostat
        self.front_camera=front_camera
        self.energy_usage=0
        self.temp=thermostat
        
    def toggle_light(self):
        self.room=input("Which Room Would you like to Turn on the lights?: ").lower()
        if self.room=="living room":
            if self.living_room_light=="OFF":
                self.living_room_light="ON"
                self.energy_usage+=5
                print(f"Living Room Light is {self.living_room_light},Energy usage is {self.energy_usage}")
            
            
        elif self.room=="bedroom":
            if self.bedroom_light=="OFF":
                self.bedroom_light="ON"
                self.energy_usage+=5
                print(f"Bedroom Light is Turned {self.bedroom_light},Energy usage is {self.energy_usage}")
                
        else:
            print("Lights Are Turned Off!")
            
            
            
    def set_temperature(self):
        self.temp=int(input("What Temperature would you like to set the room?: "))
        self.energy_usage+=10
        print(f"Temperature is set to {self.temp} F and Energy usage is {self.energy_usage}")
            
    
    def toggle_camera(self):#Fix
        self.front_camera=input("Would you like to turn on camera?: ")
        if self.front_camera=="Inactive":
            self.front_camera=="Active"
            self.energy_usage+=15
            print(f"Camera is {self.front_camera} now!")
        else:
            self.front_camera=="Inactive"
            print(f"Camera is {self.front_camera}")
            
    def show_status(self):
        print(f"Bedroom lights are {self.bedroom_light}.Living Room Lights are {self.living_room_light}.Front Camera is {self.front_camera}.Thermostat is set to {self.temp}")
        
        
    def show_energy(self):
        print(f"Total Energy is used is {self.energy_usage}")
                
    
    
    
can_home=SmartHome()
can_home.toggle_light()
can_home.set_temperature()
can_home.toggle_camera()
can_home.show_status()
can_home.show_energy()
        
        