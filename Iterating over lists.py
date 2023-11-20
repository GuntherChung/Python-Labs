import random

# Creates a new list of random numbers while being given a limit  
def generate_random_numbers(limit):
    numbers = []
    while len(numbers) < limit:
        new_number = random.randint(1,10)   # random number between 1 and 10
        numbers.append(new_number)  # Add random number to number
    return numbers

# Display the generated numbers
limit = 15
numbers = generate_random_numbers(limit)
print("Generated numbers:", numbers)

total = 0
for index, n in enumerate(numbers):
    total+= n
    print(f"{total - n } + {n} = {total}")

    # Check if n is the last element in the list
    if index == len(numbers) - 1:
        print(f"The final total is {total}")