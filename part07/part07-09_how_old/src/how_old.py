# Write your solution here

import datetime

user_day = int(input("Day: "))
user_month = int(input("Month: "))
user_year = int(input("Year: "))

user_date = datetime.datetime(user_year, user_month, user_day)

eve_date = datetime.datetime(1999, 12, 31)

age = eve_date - user_date

if eve_date > user_date:
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")
