# The full-time function will accept exp, for years worked. They have an annual pay of 25000
# if they worked from 2 - 4 years, they get a 1.5x raise and a bonus of 500
# if they worked from 4 - 10 years, they get a 2x raise and a bonus of 1000
# if they worked over 10 years, they get a 3x raise and bonus of 1500
# Anything else, they do not get a raise, their bonus is 200

def full_time(years,annual_pay=25000):
    if years>=2 and years<=4:
        print(years,"Years:",(annual_pay*1.5)+500)
    elif years>4 and years<=10:
        print(years,"Years:",(annual_pay*2)+1000)
    elif years>10:
        print(years,"Years:",(annual_pay*3)+1500)
    else:
        print(years,"Years:",(annual_pay+200))
        

