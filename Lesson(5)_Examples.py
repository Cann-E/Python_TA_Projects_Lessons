#1 Discount Program 

trip=str(input("Which kind of trip your taking?: ")).lower()
price=float(input("Whats the expected trip cost?: "))

discount= trip=="business" and price>= 1200
print("Customer Received Discount:",discount)

# if trip=="business" and price>= 1200:
#     print("Customer Received Discount:True")
# else:
#     print ("Customer Received Discount:False")
    
    
#2 Discount Code

discount_code=str(input("Please Enter Discount Code: "))

if discount_code== "winter23":
    print("%20 percent off applied")
else:
    print("Invalid code!!")
    
    
#3 Trip Recommend

trip_cost=float(input("Please Enter the trip cost: "))

if trip_cost<350:
    print("Go on a stay-cation")
if trip_cost >=350 and trip_cost<1000:
    print("Go on Road Trip")
if trip_cost > 1000:
       print("Catch a flight to the beach!") 

print("Have Fun!")

# 4 Bag Weight

flight=str(input("Domestic or International Flight ")).lower() #.lower to make all written response lowercase
bag_weight=float(input("Enter Your Bag Weight: "))


if bag_weight <= 18 :
    price=25
    print("Bag price is",price)
else:
    price=75
    print("Bag price is",price)
    
if flight=="domestic":    
    price=price+300
    print("Flight price is",price)
elif flight=="international":
    price+=750
    print("Flight price is",price)
else:
    print("Invalid Entry")
    
    

