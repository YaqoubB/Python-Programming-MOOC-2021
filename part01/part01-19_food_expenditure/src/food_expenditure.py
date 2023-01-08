# Write your solution here
cafe_trips = int(input("How many times a week do you eat at the student cafeteria?"))
cafe_cost = float(input("The price of a typical student lunch?"))
grocery_cost = float(input("How much money do you spend on groceries in a week?"))
week = (cafe_trips * cafe_cost + grocery_cost )
print("")
print("Average food expenditure:")
print(f"Daily: {week / 7} euros")
print(f"Weekly: {week} euros")