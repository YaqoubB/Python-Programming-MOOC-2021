# Write your solution here

word = str(input("Word: "))
width_1 = 28 - len(word)
width_2 = width_1 // 2

print("*" * 30)

if len(word) % 2 == 0:
    print("*" + " " * width_2 + word + " " * width_2 + "*")
else:
    print("*" + " " * width_2 + word + " " * width_2 + " *")


print("*" * 30)