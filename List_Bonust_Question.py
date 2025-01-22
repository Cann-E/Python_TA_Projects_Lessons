# BONUS CHALLENGE
# Create a function that takes a list as a parameter. If the list is 0, then return None. Otherwise, the function calculates the average of the numbers from the list.

# Create a loop to run the length of your list.

# Generate a new list every time the loop runs with the current index of your list.
# NOTE: We haven’t studied this. Here is your clue:
# sublist = numbers_list[:i+1]

# Call your function and give it the sublist.

# Print off the average grade of the sublist.

# NOTE: Every time the loop runs, it updates the average grade and your list with the next number.



numbers_list=[10, 20, 30, 40, 50]

def bonus_challenge(numbers_list):
    if len(numbers_list) ==0:
        return None
    else:
        return sum(numbers_list) / len(numbers_list)
    
for i in range(len(numbers_list)) : 
    sublist = numbers_list[:i+1]
    average=bonus_challenge(sublist)
    print(f"Sublist {i+1}: {sublist},Average: {average}")
        
    
        
    




