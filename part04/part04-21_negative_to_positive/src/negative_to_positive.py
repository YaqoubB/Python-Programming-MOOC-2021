# Write your solution here

i_pos = int(input("Please type in a positive integer: "))

i_neg = -(i_pos)

for i in range(i_neg, i_pos + 1):
    if i != 0:
        print(i)
    else:
        continue