#Conditional Statements operators  (a>b(greater)  a<b(less than)  a>=b(less than or equal)  a<=b(greater or equal)  a==b(equal)  a!=b(not equal))  operator(  and(two condition needs to be True at same time)   or(only one codition needs to be true)  )

age=int(input("Please Enter Your Age: "))

if age>=18:
    print("You Can Enter The Bar!")
else:
    print("Sorry This Place is Age Restricted to 18 and up!")
    
    
    
create_password=str(input("Please Create a Password: "))


password=str(input("Please Enter your Password: "))
if password == create_password:
    print("Welcome Back")
else:
    print("Wrong Password")