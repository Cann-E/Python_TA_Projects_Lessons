

def sum_even_numbers(numbers):
    total = 0  # Start with 0
    for num in numbers:  # Loop through each number in the list
        if num % 2 == 0:  # Check if the number is even
            total += num  # Add the number to the total if it's even
    return total

# Example usage:
my_numbers = [1, 2, 3, 4, 5, 6]  # A list of numbers
result = sum_even_numbers(my_numbers)  # Call the function
print("Sum of even numbers:", result)

    
    