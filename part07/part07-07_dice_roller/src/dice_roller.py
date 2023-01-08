# Write your solution here

import random

def roll(die: str):
    dictionary_1 = {"A":[3, 3, 3, 3, 3, 6], "B":[2, 2, 2, 5, 5, 5], "C":[1, 4, 4, 4, 4, 4]}
    return random.choice(dictionary_1[die])


def play(die1: str, die2: str, times: int):
    wins = 0
    losses = 0
    draws = 0  
    for i in range(times):
        value_1 = roll(die1)
        value_2 = roll(die2)
        if value_1 > value_2:
            wins += 1
        elif value_1 < value_2:
            losses += 1
        else:
            draws += 1
    return (wins, losses, draws)



if __name__ == "__main__":
    '''for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")'''
    play("A", "B", 10)  