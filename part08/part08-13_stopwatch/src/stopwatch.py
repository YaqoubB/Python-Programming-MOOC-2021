# Write your solution here:

import datetime

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        date = "00:00"
        self.date = datetime.datetime.strptime(date, "%M:%S")

    def tick(self):
        second = datetime.timedelta(seconds = 1)
        self.date += second


    
    def __str__(self):
        current = f"{self.date}"
        return current[14:]

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(360):
        print(watch)
        watch.tick()