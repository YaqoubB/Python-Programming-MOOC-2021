# Write your solution here

def factorials(n: int):
    my_dictionary = {}
    factorial = 1
    for i in range(1, n + 1):
        counter = i
        while counter > 0:
            factorial *= counter
            counter -= 1
        my_dictionary[i] = factorial
        factorial = 1
    return my_dictionary




if __name__ == "__main__":
    k = factorials(5)
    print(k)
    print(k[5])