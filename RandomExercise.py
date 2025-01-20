



# class Weapon():
    
#     def __init__(self,material,bullet_amount,price,mode):
#         self.material=material
#         self.bullet_amount=bullet_amount
#         self.price=price
#         self.mode=mode
        
#     def mode_(self):
#         self.wep_mode=input("Is it automatic Or Semi?: ").lower()
#         if self.wep_mode == "auto":
#             print(f"{self.wep_mode} Thats a assault rifle!")
#         else:
#             print(f"{self.wep_mode} thats a handgun")
        
#     def bullet(self):
#         self.bullet_amount=int(input("How Many Bullets your Weapon gets?: "))
#         if self.bullet_amount<30 :
#             self.mode_()
            
            
# m4=Weapon("Steel",45,100,"auto")

# m4.bullet()



# class House():
#     def __init__(self,house_age):
#         self.house_age=house_age
#         self.curr_year=2025
        
        
    
#     def house_info(self):
#         self.house_year=int(input("What year house has been built?: "))
#         self.house_age=self.curr_year-self.house_year
#         print(self.house_age)
        
#         self.house_size=int(input("How Many Square Feet is the house?: "))
#         if self.house_size>2000:
#             print(f"{self.house_size} Thats A good house size!")
#             self.house_rooms=int(input("How Many rooms in this house?: "))
#             if self.house_rooms>5:
#                 print(f"{self.house_rooms} that good amount of rooms in the house!")
#             else:
#                 print(f"{self.house_rooms} that not that much of rooms!")
#         else:
#             print(f"{self.house_size} that not that good amount of a house size!")
            
#     def house_price(self):
#         self.price=int(input("Whats the Price of this house(k amount(k amount)?: "))
#         if self.price >300 and self.house_size>2000:
#             print(f"{self.house_size} is a good house size for {self.price} k usd!")
#         elif self.price >300 and self.house_size<2000:
#              print(f"{self.house_size} is a small house size for {self.price} k usd!") 
#         else:
#             print(f"{self.house_size} house size is not that expensice its only {self.price} k usd!") 
            
            
# house_porter=House(2010)
# house_porter.house_info()
# house_porter.house_price()
        
            
            


class Computer():
    
    def __init__(self,owner_info,purchase_date):
        self.owner_info=owner_info
        self.purchase_date=purchase_date
        
    
    def computer_brand(self):
        self.computer_b=input("Whats the brand of the computer:? ")
    
    def computer_specs(self):
        self.processor_="intel i7"
        self.gpu_="RTX 4080"
        self.ram_="64 GB DDR4"
        
    def computer_price(self):
        self.price_=float(input("How much you paid for your Computer(k price)?: "))
        if self.price_<2 :
            print(f"{self.price_}k Thats a Bargain")
        else:
            print(f"{self.price_}k Thats expensive!")
        
class Alienware(Computer):
    
    def __init__(self,owner_info,purchase_date,screen_size,weight):
       super().__init__(owner_info,purchase_date)
       self.screen_size=screen_size
       self.weight=weight
       self.operating_system="Not Set"
       
    def screen_resolution(self):
        self.resolution=input("Whats the Resolution of your Screen?: ").upper()
        if self.resolution=="1080P":
            print(f"{self.resolution} Thats Low Resolution")
        elif self.resolution=="2K":
            print(f"{self.resolution} Thats a Good Enough Resolutiuon!")
        elif self.resolution=="4K":
            print(f"{self.resolution} Thats very High Resolution!")
            
        
    def change_operating_system(self):
        
        while True:
            self.change_=input("Would you like to change Operating System in the Alienware!?: ").lower()
            if self.change_=="yes":
                self.response_1=input("What would you like the new Operating Software to be?: ").lower()
                if self.response_1=="windows":
                    self.yes_no=input("Are You sure there is no going back Yes/No: ").lower()
                    if self.yes_no=="yes":
                        print("Operating System changed Succesfully!")
                        self.operating_system=self.response_1
                        break
                    else:
                        print("Operation Aborted")
                        break
                elif self.response_1=="linux":
                    self.yes_no=input("Are You sure there is no going back Yes/No: ").lower()
                    if self.yes_no=="yes":
                        print("Operating System changed Succesfully!")
                        self.operating_system=self.response_1
                        break
                    else:
                        print("Operation Aborted")
                        break
            elif self.change_=="no":
                print("OS change aborted!")
    
           
           
laptop1=Alienware("Can","November 02","17 inch","10 lbs")
laptop1.computer_brand()
laptop1.computer_specs()
laptop1.screen_resolution()
laptop1.computer_price()
laptop1.change_operating_system() 


print("Brand:",laptop1.computer_b,"It costed:",laptop1.price_)
print(f"Graphics Card {laptop1.gpu_}")
print(f"Processor is {laptop1.processor_}")
print(f"Your ram size is {laptop1.ram_}")
print(f"Your Screen Resolution is {laptop1.resolution}")
print(f"Your New operating System is {laptop1.operating_system}")

  
   

    
           
        
