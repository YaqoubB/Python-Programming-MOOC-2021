# Write your solution here
# Remember the import statement
# from datetime import date

import datetime

def list_years(dates: list):
    list_1 = []
    for i in dates:
        year = i.year
        list_1.append(year)
    return sorted(list_1)


if __name__ == "__main__":
    date1 = datetime.date(2019, 2, 3)
    date2 = datetime.date(2006, 10, 10)
    date3 = datetime.date(1993, 5, 9)
    years = list_years([date1, date2, date3])
    print(years)