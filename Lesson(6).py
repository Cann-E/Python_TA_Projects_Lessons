#Nesting Conditions .lower() .upper()  .capitalize()

gender=input("Select Gender M/F: ").upper()
age=int(input("Enter Age: "))

if age>=18 :
    if gender=="M" :
        print("You can Enter My Boy!")
    elif gender=="F":
        print("You can Enter My Girl!!")
elif age<18:
    if gender=="M":
        print("You too young my boi!")
    elif gender=="F":
        print("You too young my girl!!")
else:
    print("I dont know you mate!")

