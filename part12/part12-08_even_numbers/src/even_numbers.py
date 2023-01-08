# Write your solution here

def even_numbers(beginning: int, maximum: int):
    number = beginning
    while number <= maximum:
        if number % 2 == 0:
            yield number
            number += 2   #could number += 2 to perm chain even numbers
        else:
            number += 1


if __name__ == "__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)