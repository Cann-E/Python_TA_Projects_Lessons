#User Input int() str() float()

name=input("Please Enter Your Name: ")
age=input("Please Enter Your Age: ")
sex=input("Please Enter Your Sex: ")
weight=input("Please Enter Your Weight: ") #input is string
height=input("Please Enter Your Height: ")

print("You are",name,"and your age is:",age,"Your sex is:",sex,"You weight",weight,"lbs","and you are",height,"inches tall.")
#total=age+10 !!!wrong cause its string 

#int() allows converting string to integer
#str() allows converting integer to string

age=int(age)
total=age+10
print("Your new age after 10 years is",total)

age=str(age)
age_name=age+"can"
print("New Name is:",age_name)

