number = int(input("Please type in a number: "))
counter_a = 1
counter_b = 1

while number > 0 and counter_a <= number:
    while counter_b <= number:
        print(f"{counter_a} x {counter_b} = {counter_a * counter_b}")
        counter_b += 1
    counter_a += 1 
    counter_b = 1 


