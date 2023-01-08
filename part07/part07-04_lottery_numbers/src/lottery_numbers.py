# Write your solution here

import random

def lottery_numbers(amount: int, lower: int, upper: int):
    list_1 = list(range(lower, upper + 1))
    list_random = random.sample(list_1, amount)
    return sorted(list_random)



if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)