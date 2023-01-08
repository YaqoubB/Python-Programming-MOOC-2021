# Write your solution here
gift = int(input("Value of gift: "))

if 5000 <= gift < 25000:
    print(f"Amount of tax: {100 + (gift-5000) * 0.08} euros")
elif 25000 <= gift < 55000:
    print(f"Amount of tax: {1700 + (gift-25000) * 0.1} euros")
elif 55000 <= gift < 200000:
    print(f"Amount of tax: {4700 + (gift-55000) * 0.12} euros")
elif 200000 <= gift < 1000000:
    print(f"Amount of tax: {22100 + (gift-200000) * 0.15} euros")
elif 1000000 <= gift:
    print(f"Amount of tax: {142100 + (gift-1000000) * 0.17} euros")

else:
    print("No tax!")