# #1

create_passcode=input("Please Create a passcode: ")
invalid="!@#$%^&*_+"

for i in create_passcode:
    if i in invalid:
        print(i,"Invalid Character")
        
        


#2

word=input("Please Enter a single word: ")
vowels="aeiou"
count=0

for i in word:
    if i in vowels:
        print(i,"These are vowels!")
        count+=1

print("Vowel count is:",count)


#3


phone_number=input("Please Enter Phone Number: ")
valid="1234567890"

for i in phone_number:
    if i not in valid:
        print("Invalid Phone Number")
        break
else:
    print("Valid Number")
        





#4


guests=int(input("Please Enter Guest Number: "))

for i in range(guests):
    name=input("Please Enter Your Name: ")
    age=int(input("Please Enter Your age: "))
    if age>=18:
        print("Welcome!!",name)
    else:
        print("You are too young to drink!",name)




#5
    
chance=5
tries=1

for i in range(chance):
    username=input("Please Enter Username: ")
    password=input("Please Enter Password: ")
    if username =="admin" and password=="12345":
        print("Welcome back!")
        break
    tries+=1

if username !="admin" or password !="12345":
    print("Your not the admin!")
    
print("It took you",tries,"tries")

        
    

        