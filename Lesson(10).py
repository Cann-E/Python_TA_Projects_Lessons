#Modules ex: import random

from functions_Can import * #using functions_Can Module

#1


people_count=int(input("How Many People You want to calculate: "))

while people_count>0:
    name=input("Whats your first and last name: ")
    weight=int(input("Please Enter your weight?(KG): "))
    height=float(input("Please Enter your height(Meters)?: "))
    show_BMI(weight,height)
    people_count-=1




#2

main_() 



#3

response_1=input("Would you like to check your flight?(yes/quit): ").lower()

while response_1=="yes":
    main_()
    response_1=input("Would you like to check your flight?(yes/quit): ").lower()
    if response_1=="quit":
        break
