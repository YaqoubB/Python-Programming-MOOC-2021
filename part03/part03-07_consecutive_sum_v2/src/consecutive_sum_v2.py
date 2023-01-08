# Write your solution here

limit = int(input("Limit: "))
number = 1
word1 = "1"
sum = 0
flag = True

while sum <= limit and flag:
    sum += number
    number += 1
    if sum >= limit:
        flag = False
    if flag == True:
        word1 += f" + {number}"
    
print(f"The consecutive sum: {word1} = {sum}")