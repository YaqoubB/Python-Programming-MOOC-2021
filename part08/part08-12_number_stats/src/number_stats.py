# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.sum = 0


    def add_number(self, number:int):
        self.counter += 1
        self.sum += number
        
    def count_numbers(self):
        return self.counter
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.sum == 0:
            return (self.sum)
        else:
            return (self.sum / self.counter)

integers = NumberStats()
even_integers = NumberStats()
odd_integers = NumberStats()

while True:
    number = int(input("Please type in integer numbers: "))
    if number == -1:
        print(f"Sum of numbers: {integers.get_sum()}")
        print(f"Mean of numbers: {integers.average()}")
        print(f"Sum of even numbers: {even_integers.get_sum()}")
        print(f"Sum of odd numbers: {odd_integers.get_sum()}")
        break
    elif number % 2 == 0:
        even_integers.add_number(number)
    else:
        odd_integers.add_number(number)
    integers.add_number(number)

        

