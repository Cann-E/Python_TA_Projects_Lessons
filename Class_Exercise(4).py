from time import sleep

class Bank_Account():
    def __init__(self,account_balance):
        self.account_balance=account_balance
        
    def deposit_money(self):
        self.deposit=int(input("How Much Money Would you like to Deposit?: "))
        self.account_balance+=self.deposit
        print(f"Your New Balance is {self.account_balance} $")
        
    def withdraw_money(self):
        self.withdraw=int(input("How much money would you like to withdraw:? "))
        if self.withdraw>self.account_balance:
            print("Insufficient Funds!!!")
        else:
            self.account_balance-=self.withdraw
            print(f"You withdraw {self.withdraw} $")
            print(f"New Balance is {self.account_balance} $")
            
    def check_balance(self):
        print(f"Your Current Balance is: {self.account_balance} $")
        
    def run(self):
        while True:            
            response_1=input("Welcome to Chase Bank\n"
                             "1-Deposit Money \n"
                             "2-Withdraw Money \n"
                             "3-Check Balance \n"
                             "4-Send Money \n"
                             "5-Exit \n" 
                             ": "                                                        
                                     ).lower()
            sleep(1)
            
            if response_1=="1" or response_1=="deposit money":
                self.deposit_money()
                
            elif response_1 =="2" or response_1=="withdraw money":
                self.withdraw_money()
                
            elif response_1=="3" or response_1 =="check balance":
                self.check_balance()
            
            elif response_1=="5" or response_1 =="exit":
                print("Thank you for Banking with Chase Bank!")
                break
            elif response_1=="4" or response_1 =="send money":
                self.send_money()
    
    def send_money(self):
        self.send_=int(input("How Much would you like to send?: "))
        self.receiver=input("Who would you like to send?: ")
        
        if self.account_balance<self.send_:
            print("Insuficcient Funds!!!!!")
        else:
            self.account_balance-=self.send_
            print(f"You sent {self.send_}$ to {self.receiver}")
    
            
can_ercan=Bank_Account(5000) 
can_ercan.run()           