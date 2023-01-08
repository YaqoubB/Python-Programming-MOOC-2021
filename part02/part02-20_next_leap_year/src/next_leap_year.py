# Write your solution here
year = int(input("Year: "))
year_1 = year + 1
year_2 = year + 2
year_3 = year + 3
year_4 = year + 4

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    if year_4 % 4 == 0 and year_4 % 100 == 0 and year_4 % 400 != 0:
        print(f"The next leap year after {year} is {year + 8}")
    else: print(f"The next leap year after {year} is {year + 4}")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print(f"The next leap year after {year} is {year + 4}")
elif year % 4 == 1:
    if year_3 % 4 == 0 and year_3 % 100 == 0 and year_3 % 400 != 0:
        print(f"The next leap year after {year} is {year + 7}")
    else:
        print(f"The next leap year after {year} is {year + 3}")
elif year % 4 == 2:
    if year_2 % 4 == 0 and year_2 % 100 == 0 and year_2 % 400 != 0:
        print(f"The next leap year after {year} is {year + 6}")
    else:
        print(f"The next leap year after {year} is {year + 2}")
elif year % 4 == 3:
    if year_1 % 4 == 0 and year_1 % 100 == 0 and year_1 % 400 != 0:
        print(f"The next leap year after {year} is {year + 5}")
    else:
        print(f"The next leap year after {year} is {year + 1}")


        


    
    
