# Write your solution here
tempf = int(input("Please type in a temperature(F):"))
tempc = ((tempf - 32) * (5/9))
print(f"{tempf} degrees Fahrenheit equals {tempc} degrees Celsius")
if tempc < 0:
    print("Brr! It's cold in here!")