

# 1- Create 4 functions, The first 3 will be terminal_1, terminal_2, terminal_3
# When one of those functions is called it prints off which terminal to go to, then calls the main function again
# The main function should ask 'Is your flight a budget/domestic or international:' when called
# budget - terminal_1   -   domestic - terminal_2   -   international - terminal_3


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
        

main_()       
    



# 2- POPULAR - Create a BMI calculator using 2 functions
# One function calculates and returns the BMI (BMI = weight / (height * height) )
# The second function takes the BMI results and tells you if you're Underweight, Normal or Overweight
# Create a loop to run for the number of people there are
# Pass the weight and height into one of the functions which will call the first function




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
        
        
people_count=int(input("How Many People You want to calculate: "))

while people_count>0:
    name=input("Whats your first and last name: ")
    weight=int(input("Please Enter your weight?(KG): "))
    height=float(input("Please Enter your height(Meters)?: "))
    show_BMI(weight,height)
    people_count-=1






