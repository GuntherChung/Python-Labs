import random

class MathProcesses:
    def __init__(self, limit):
        self.limit = limit
        self.numbers = []

    def generate_random_numbers(self):
        while len(self.numbers) < self.limit:
            new_number = random.randint(1, 10)
            self.numbers.append(new_number)

    def sort_numbers(self):
        self.numbers = sorted(self.numbers)

    def calculate_sum(self):
        total = 0
        for index, n in enumerate(self.numbers):
            total += n
            print(f"{total - n} + {n} = {total}")
        print(f"The final total is {total}")

    def calculate_factorial(self, number):
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial