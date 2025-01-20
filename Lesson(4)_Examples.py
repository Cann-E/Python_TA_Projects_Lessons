
#2 USE NESTING

# car_rental_price_oneday=input("Please enter the rental price per day: ")
# rent_days_count=input("How many days you want to rent?: ")

# car_rental_price_oneday=float(car_rental_price_oneday)
# rent_days_count=int(rent_days_count)

car_rental_price_oneday=float(input("Please enter the rental price per day: "))
rent_days_count=int(input("How many days you want to rent?: "))

total_cost=(rent_days_count*car_rental_price_oneday)

print("Per Day price is:",car_rental_price_oneday,"You want to rent for:",rent_days_count,"days And the total cost for this rental is:",total_cost)


#3

# package1=input("Please Enter First Package Weight: ")
# package1=float(package1)

package1=float(input("Please Enter First Package Weight: "))

# package2=input("Please Enter Second Package Weight: ")
# package2=float(package2)

package2=float(input("Please Enter Second Package Weight: "))

# package3=input("Please Enter Third Package Weight: ")
# package3=float(package3)

package3=float(input("Please Enter Third Package Weight: "))

total_orig=(package1+package2+package3)
discounted_price=((package1+package2+package3)*0.8)

print("Your original price for the shipment is:",total_orig,"but we gave you a %20 percent discount so your new price is:",discounted_price)
