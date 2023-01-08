# Write your solution here

import fractions

def fractionate(amount: int):
    list_1 = []
    number = fractions.Fraction(1, amount)
    for i in range(0, amount):
        list_1.append(number)
    return list_1



