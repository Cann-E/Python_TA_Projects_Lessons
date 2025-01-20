from time import *


stopwatch=int(input("1 start 0 end: "))

while stopwatch!=0:
    start_timer=time()
    stopwatch=int(input("1 cont 0 end: "))
    
end_timer=time()
time_passed=end_timer-start_timer
print(round(time_passed,1))

points=0
if time_passed<10:
    points+=3
elif time_passed>10 and time_passed<15:
    points+=2
else:
    points+=1

print("Points awarded is:",points)
