# Write your solution here

limit = int(input("Limit: "))
number = 1
sum = 0
flag = True

while sum <= limit and flag:
    sum += number
    number += 1
    if sum == limit:
        flag = False
        

print(sum)