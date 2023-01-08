# Write your solution here

word = str(input("Please type in a string: "))
index_a = word[1]
index_b = word[-2]

if index_a == index_b:
    print(f"The second and the second to last characters are {index_a}")
else:
    print("The second and the second to last characters are different")