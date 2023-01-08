# Write your solution here

reply = ""

while True:
    reply = str(input("Please type in a string: "))
    print(reply)
    print("-" * len(reply))
    if len(reply) == 0:
        break

