# Write your solution here

password = input("Password: ")
while True:
    password_rep = input("Repeat password: ")
    if password_rep == password:
        break
    print("They do not match!")

print("User account created!")
    
