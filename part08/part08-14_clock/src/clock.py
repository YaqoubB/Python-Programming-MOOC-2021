# Write your solution here:

import datetime

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        date = f"{hours}:{minutes}:{seconds}"
        self.date = datetime.datetime.strptime(date, "%H:%M:%S")


    def tick(self):
        second = datetime.timedelta(seconds = 1)
        self.date += second

    def set(self, hrs: int, mins: int):
        date2 = f"{hrs}:{mins}:00"
        self.date = datetime.datetime.strptime(date2, "%H:%M:%S")
    
    def __str__(self):
        current = f"{self.date}"
        return current[11:]


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    clock.set(12, 5)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
