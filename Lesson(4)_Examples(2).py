#1
income=float(input("How Much Money Do You Make?: "))


food=float(input("How Much Do you spend on food?: "))
rent=float(input("How Much Do you Spend on rent?: "))
electric=float(input("How much Do you spend on Electric?: "))
insurance=float(input("How much your insurance Cost?: "))
expense_total=(food+rent+electric+insurance)

total=(income-expense_total)

print("You make",income,"and your monthly total expenses are",expense_total,"So after expenses",total,"dollar left to use.")

#2

monthly_pay=float(input("Please Enter Your Monthly Pay: "))
extra_hours=float(input("Please Enter Your Extra Hours Worked: "))
bonus=((monthly_pay*0.20)*extra_hours)

print("Overtime Bonus Pay is: ",bonus)