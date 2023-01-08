# Write your solution here

import datetime

'''filename = "first_of_may.txt"
start_date = "1.5.2020"
days_number = 1'''

filename = input("Filename: ")
start_date = input("Starting date: ")
days_number = int(input("How many days: "))

with open(filename, "w") as file:
    pass

with open(filename, "a") as file:
    content = []
    starting_date_1 = datetime.datetime.strptime(start_date, "%d.%m.%Y")
    starting_date_2 = starting_date_1.strftime("%d.%m.%Y")
    if days_number > 1:
        time_delta_total = datetime.timedelta(days = days_number - 1)
        ending_date_1 = starting_date_1 + time_delta_total
        ending_date_2 = ending_date_1.strftime("%d.%m.%Y")
    else:
        ending_date_2 = starting_date_2
    content.append(f"Time period: {starting_date_2}-{ending_date_2}")
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    time_delta = datetime.timedelta(days = 1)
    sum = 0
    screen_datetime = starting_date_1
    for i in range(days_number):
        screen_date = screen_datetime.strftime("%d.%m.%Y")
        screen_time = input(f"Screen time {screen_date}: ")
        screen_time_summing = screen_time.split(" ")
        for i in screen_time_summing:
            sum += int(i)
        screen_time = screen_time.replace(" ", "/")
        content.append(f"{screen_date}: {screen_time}")
        screen_datetime += time_delta
    total_minutes = f"Total minutes: {sum}"
    avg_minutes = f"Average minutes: {sum / days_number:.1f}"
    content.insert(1, total_minutes)
    content.insert(2, avg_minutes)
    print(f"Data stored in file {filename}")
    with open(filename, "a") as file:
        for i in content:
            line = i[:]
            file.write(line+"\n")





    
        
    