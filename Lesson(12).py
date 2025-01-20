#Time Module round(variable,number of decimals)
from time import *

#1


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



#2



stopwatch=int(input("1 start 0 end: "))

while stopwatch!=0:
    start_timer=time()
    stopwatch=int(input("1 cont 0 end: "))
    
end_timer=time()
time_passed=end_timer-start_timer


new_time=round(time_passed,0)
while time_passed>0:
    print(round(time_passed,0))
    time_passed-=1
    
print("Countdown finished after",new_time,"Seconds")


############################ALTERNTAE 2 sleep(number)

countdown_start=int(input("Please Enter Countdown Seconds: "))

amount=countdown_start

while amount>0:
    print("Countdown:",amount)
    amount-=1
    sleep(1)
    

print("Countdown finished after",countdown_start,"Seconds")    






#3


file_size=int(input("Enter File Size(MB): "))
internet_speed=int(input("Enter Internet Speed(Megabits/Seconds): "))


download_time=(file_size*8)/internet_speed
print("Your Download is gonna take",download_time,"Seconds")

curr_time=download_time
while download_time>0:
    print("Downloading:",round(download_time,0))
    download_time-=1
    sleep(1)
    
print("Download Complete:","It took:",curr_time,"Seconds")

