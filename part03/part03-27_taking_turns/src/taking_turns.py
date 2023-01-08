# Write your solution here
number = int(input("Please type in a number: "))
counter = 0
counter_1 = 1

if number ==1:
    print(1)

if number == 2:
    print(1)
    print(2)

elif number % 2 == 0:
    while counter_1 < number:
        print(counter_1)
        print(number - counter)
        counter_1 += 1
        counter += 1
        if counter +1 > number - counter:
            break
    

if number % 2 != 0:
    while counter_1 < number:
        print(counter_1)
        if counter_1 == number - counter:
            break
        print(number - counter)
        counter_1 += 1
        counter += 1