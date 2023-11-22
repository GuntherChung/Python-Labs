import random

class MathProcesses:
    def __init__(self, limit):
        self.limit = limit
        self.numbers = []

    def generate_random_numbers(self):
        while len(self.numbers) < self.limit:
            new_number = random.randint(1, 10)
            self.numbers.append(new_number)
        self.numbers = sorted(self.numbers)
        print(f"generated random numbers: {self.numbers}")

    def calculate_sum_of_list(self):
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