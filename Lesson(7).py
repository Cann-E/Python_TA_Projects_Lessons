#While Loops

# count=10

# while count>0 :
#     count=count-1
#     print(count)
    
create_password=(input("Please Create a Password: "))
print("Thank you Your password has been created!")

password=(input("Please Enter Your password: "))

while password !=create_password:
    print("You have entered the wrong password!!")
    password=input("Please Try again: ")
print("Welcome back to your account!!")


