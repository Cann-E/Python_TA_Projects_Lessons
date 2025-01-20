
#1

name=input("Please Enter your Name: ")
country=input("Please Enter Your Country: ")
city=input("Please Enter Your City: ")

print("Your Name is:",name,"and your Country is:",country,"and You live in:",city,"city")

#2

car_rental_price_oneday=input("Please enter the rental price per day: ")
rent_days_count=input("How many days you want to rent?: ")

car_rental_price_oneday=float(car_rental_price_oneday)
rent_days_count=int(rent_days_count)

total_cost=(rent_days_count*car_rental_price_oneday)

print("Per Day price is:",car_rental_price_oneday,"You want to rent for:",rent_days_count,"days And the total cost for this rental is:",total_cost)

#3

package1=input("Please Enter First Package Weight: ")
package1=float(package1)

package2=input("Please Enter Second Package Weight: ")
package2=float(package2)

package3=input("Please Enter Third Package Weight: ")
package3=float(package3)

total_orig=(package1+package2+package3)
discounted_price=((package1+package2+package3)*0.8)

print("Your original price for the shipment is:",total_orig,"but we gave you a %20 percent discount so your new price is:",discounted_price)


#4

user_id=786147
name=input("Please Enter Your Name: ")
age=input("Please Enter Your age: ")

user_id=str(user_id)
name=str(name)
age=str(age)

print("Your user id is:",user_id,"and your name is",name,"and your age is",age)  #another version  print("Your user id is: "+user_id+" and your name is "+name+" and your age is "+age) using concatination