import random
answers=list()

fruit=input("Please Enter the fruit you want to add the list(quit to stop): ")

while fruit != "quit":
    empty_list.append(fruit)
    fruit=input("Please Enter the fruit you want to add the list(quit to stop): ")
    
guess_=input("Please Guess the fruit in the list: ")

print(empty_list)


for answer in answers:
  if guess_== answer:
      print("Congrats!")
      break
  else:
      print("Wrong")
      break
        
    
    



capital_city=[]
city_name=input("Enter the city name(0 to quit): ")

while city_name != "0":
    if city_name in capital_city:
        print(f"{city_name} is already in the list!")
        city_name=input("Enter the city name(0 to quit): ")
    else:
        capital_city.append(city_name)
        print(f"{city_name} added to your list!")
        city_name=input("Enter the city name(0 to quit): ")
        
capital_city.sort()

print(f"These are all the cities you entered: {capital_city}")




basketball_player="can tolga erim emre murat"
basketball_player=basketball_player.split(" ")
print(f"Players are :{basketball_player}")

size=len(basketball_player)
print(size)

teams=[]

for player in basketball_player:
    random_team=random.randint(1,3)
    teams.append(random_team)


for i in range(size):
    
    size-=1
    print(f"{basketball_player[i]} plays in team number {teams[i]}")
    
    
    



list=["Billy - 5","Sarah - 4","Leo - 3","John - 3","Anna - 4"]

average_score=0

for score in list:
    x=int(score[len(score)-1])
    average_score+=x
    
average_score /= len(list)

print("The Average Score: ", average_score)


    


     
    