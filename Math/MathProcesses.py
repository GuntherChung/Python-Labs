import random

class MathProcesses:
    """ The purpose of this class is to hold multiple math processing methods.
    The general purpose of this overall goal is brush up on code techniques.
    Also, by writing a class with multiple methods, I am to strengthen my skills
    with dependencies and nesting.  
    """
    def __init__(self, limit):
        """The initialization of the self for MathProcess

        Args:
            limit (int): Take in a value for the limit for the length for the
            list in the function generate_random_numbers.
        """
        self.limit = limit
        self.numbers = []

    def generate_random_numbers(self):  # define function generate_random_numbers
        """Generate random numbers that will be stored in self.numbers as a list.
        """
        while len(self.numbers) < self.limit:   # While the length of self.numbers is less than self.limit
            new_number = random.randint(1, 10)      # Assign a random int between 1:10 to a new variable "new_number" 
            self.numbers.append(new_number)         # Append new_number to self.numbers
        self.numbers = sorted(self.numbers)     # Sort the items in self.numbers
        print(f"generated random numbers: {self.numbers}")  # Print results 

    def calculate_sum_of_list(self):    # define function calculate_sum_of_list
        total = 0
        for index, n in enumerate(self.numbers):
            total += n
            print(f"{total - n} + {n} = {total}")
        print(f"The final total is {total}")

    def calculate_factorial(self, number):
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print (f"Factorial of {number} = {factorial}")
    
    def prod_of_two_nums(self):
        first = self.numbers[random.randint(1,10)]
        second = self.numbers[random.randint(1,10)]
        print (f"From the random number list, {first} x {second} = {first*second}")
    
process = MathProcesses(limit=10)
process.generate_random_numbers()
process.calculate_sum_of_list()
process.calculate_factorial(number=4)
process.prod_of_two_nums()