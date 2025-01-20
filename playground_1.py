#Calculator

num1=float(input("Please Enter First Number: "))
num2=float(input("Please Enter Second Number: "))

operator=input("Please Choose your Operator: ")

if operator == "+":
    print (num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*" :
    print(num1*num2)
elif operator == "/" :
    print(num1/num2)
else:
    print("Invalid Operator Try again!")


#Hobbies

temperature=float(input("Whats the temperature Right Now?: "))  # 5,10,15,20,30,50
time=int(input("What time is it?: "))  #swimming,soccer,skiing,indoors,nothing,video game

if temperature >= 50  and time > 10 :
    print("Its too late and hot better play some video games!!")
elif temperature >=50  and time <10:
    print("Its to hot but its not that late so you can either play video games or stay indoors or do nothing!")
elif temperature <=30 and time >10:
    print("Its hot but not scorching but its late so you can either stay indoors or play video games!")
elif temperature <= 30 and time <10:
    print("Its hot but not scorching and its not late so you can go swimming or play video games!")
elif  temperature <=10 and time <10:
    print ("Wheather is cold but not freezing and its not that late so you can eaither play soccer or watch tv!")

    
print("Anyways Have fun!!!")

