

class Phone():
    def __init__(self,brand,color,phone_number):
        self.brand=brand
        self.color="None"
        self.phone_number="None"
        self.price=0
        
    def make_call(self,phone_number):
        self.phone_number=phone_number     
        print(f"Calling {self.phone_number}")
        
    def send_txt(self,txt_phone_number,message):
        self.txt_phone_number=txt_phone_number
        self.message=message
        print(f"Sending.. {self.message} to {txt_phone_number}")
        
    def check_battery(self,battery):
        self.battery=battery
        print(f"Battery is at {self.battery} percent.")
        
    def take_Photo(self):
        print("Photo Taken!")
        
    def lock_phone(self):
        print("Phone is now locked!!")
        
can_phone=Phone("Iphone","Black","832-844-9059")

can_phone.make_call("346-247-8669")

can_phone.send_txt("346-247-8660","What's up dude? ")

can_phone.check_battery("% 93")

can_phone.take_Photo()

can_phone.lock_phone()
          
          
          
