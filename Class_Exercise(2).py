

class SmartPhone():
    
    def __init__(self,brand,color,phone_number):
        self.brand=brand
        self.color=color
        self.phone_number=phone_number
        self.battery=100
        self.apps=[]
    
    def make_call(self,phone__number):
        self.phone__number=phone__number
        
        while self.battery>0:
            self.call_=input("Would you like to make a call? Y/N: ").upper()
            
            if self.call_=="Y":
                self.battery-=5       
                print(f"Calling... {self.phone__number} Battery is now {self.battery}")
                
            elif self.call_=="N":
                print("Terminationg the call!")
                break
            
            else:
                print("Wrong Input Pls Try again!: ")
        else:
            print("Battery Too Low!!!")
            
            
    def send_text(self,number,message):
        self.number=number
        self.message=message
        
        self.battery-=3
        print(f"Sending...{self.message} to {self.number} and Battery percentage is {self.battery}")
        
        
    def install_app(self):
        
        
        while self.battery>0:
            self.app=input("What app would you like to download?(Type 'exit' to cancel): ").capitalize()
            while self.app != "Exit":
                self.apps+=self.app
                self.battery-=10
                print(f"Installed: {self.app} . Battery percent is {self.battery}.")
                self.app=input("Would you like to add more apps?(Type 'exit' to cancel): ").capitalize()
            else:
                print("App install is Terminated!")
                break
            
            
    def check_apps(self):
        if self.apps:  
            print(f"Installed apps: {','.join(self.apps)}")
        else:
            print("No Apps Installed!")
        
        
    
                
            
            
            
            
            
            
            
            
            
can_iphone=SmartPhone("Iphone","Black","832-844-9059")

can_iphone.make_call("734-657-9043")

can_iphone.send_text("835-123-4569","Whats up!")

can_iphone.install_app()

can_iphone.check_apps()