# TEE RATKAISUSI TÄHÄN:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year 
        
    def days(self):
        return (self.__day +  (self.__month * 30) + (self.__year * (12 * 30)))


    def __lt__(self, another):
        return self.days() < another.days()

    def __gt__(self, another):
        return self.days() > another.days()
    
    def __eq__(self, another):
        return self.days() == another.days()

    def __ne__(self, another):
        return self.days() != another.days()

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __add__(self, add_days):
        if add_days >= 0:
            total = self.days() + add_days
            years = total // 360
            months = (total - (years * 360)) // 30
            days = total - (years * 360) - (months * 30)
        return SimpleDate(days, months, years)

    def __sub__(self, sub_year):
        return abs(self.days() - sub_year.days())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)