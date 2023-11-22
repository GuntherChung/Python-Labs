import random

# Creates a new list of random numbers while being given a limit  
def generate_random_numbers(limit):
    numbers = []
    while len(numbers) < limit:
        new_number = random.randint(1,10)   # random number between 1 and 10
        numbers.append(new_number)  # Add random number to number
    sorted_numbers = sorted(numbers) # logarithmically sort list of numbers 
    return sorted_numbers

# Display the generated numbers
limit = 10
numbers = generate_random_numbers(limit)
print("Generated numbers:", numbers)

# Iterates over provided list to add up all of the numbers.
def sum_of_list(list):
    total = 0
    for index, n in enumerate(list):
        total+= n   # Addition
        print(f"{total - n } + {n} = {total}")  # Process print out
    return print(f"The final total is {total}") # Final product

sum_of_list(numbers)