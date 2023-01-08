# Write your solution here

def prime_numbers():
    number = 2
    if number == 2:
        yield 2
        number += 1
    while True:
        for i in range(2, number):
            flag = True
            if number % i == 0:
                number += 1
                flag = False
                break
        if flag:
            yield number 
            number += 1



if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))