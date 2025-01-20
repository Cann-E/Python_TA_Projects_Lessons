# In the main program, create a loop to start and quit the program
# Every time it runs, it'll ask for an employee name and type (salary or hourly)
# if type = hourly, ask for number of hours worked and use the hourly function in a variable
# if type = salary, ask for years worked and use the full-time function in a variable
# Anything else, print off "You are unemployed!"
# At the loop end, print off the employees' name and their pay rate


from Hourly_Emplyees import hourly_function
from Fulltime_Employees import full_time








system_=int(input("Do you want to start the program(1 to start 0 to end!): "))

while system_ !=0:
    
    fullname=input("Please Enter Your Full Name: ")
    salary_type=input("Salary or Hourly?: ").lower()
    
    if salary_type=="hourly":
        hours=int(input("Please Enter Your hours: "))
        print(hourly_function(hours))
    elif salary_type=="salary":
        years=int(input("How Many Years you been working here?: "))
        full_time(years)
    else:
        print("You are Unemplyed!")
        
    print("Name:",fullname)
    print("Pay Type:",salary_type)
    
    system_=int(input("Do you want to start the program(1 to start 0 to end!): "))
