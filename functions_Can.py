def print_name(name):
    print("Name:",name)
    
def print_age(age):
    print("Age:",age)



#################################################### 
    
    
    
     
def person():
    first_name=input("Whats Your name: ")
    last_name=input("Whats Your Last name: ")
    age=int(input("How old are you: "))
    sex=input("Whats Your gender: ")
    country=input("Where are you from: ")
    print(first_name,last_name)
    print("Age is:",age)
    print("You are:",sex)
    print("Your from:",country)
    
    
    
    
################################################## 
    
    
    
    
def bmi_calculator(weight,height):
    BMI = weight / (height * height)
    return BMI



def show_BMI(weight,height):
    result=bmi_calculator(weight,height)
    if result<18.5:
        print("Underweight! BMI Is:",result)
    elif result>=15 and result<=24.9:
        print("Normal weight!! BMI Is:",result)
    else:
        print("Overweight!!! BMI Is:",result)
        
        

    
    
#################################################
    
    
def terminal_1():
    print("Go to Terminal 1")
    
    
def terminal_2():
    print("Go to Terminal 2")
    
    
def terminal_3():
    print("Go to Terminal 3")    
    

def main_():
    while True:
        response_1=input("Is your flight budget, domestic, or international?(exit to end program): ").lower()
        if response_1=="budget":
            terminal_1()
        elif response_1=="domestic":
            terminal_2()
        elif response_1=="international":
            terminal_3()
        if response_1=="exit":
            break
        

         
    