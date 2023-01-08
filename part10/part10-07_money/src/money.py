# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        return f"{self.__euros}.{self.__cents} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents
    
    def __lt__(self, another):
        return self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents)

    def __gt__(self, another):
        return self.__euros > another.__euros or (self.__euros == another.__euros and self.__cents > another.__cents)

    def __add__(self, another):
        money = ((self.__euros + another.__euros) * 100)  + (self.__cents + another.__cents)
        money = money / 100
        money = str(money)
        money = money.split(".")
        money_decimal = money[1]
        if len(money_decimal) == 1:
            money_decimal = f"{money_decimal}0"
        return Money(int(money[0]), int(money_decimal))
    
    def __sub__(self, another):
        if self.__gt__(another) or self.__eq__(another):
            money = ((self.__euros - another.__euros) * 100)  + (self.__cents - another.__cents)
            money = money / 100
            money = str(money)
            money = money.split(".")
            money_decimal = money[1]
            if len(money_decimal) == 1:
                money_decimal = f"{money_decimal}0"
            return Money(int(money[0]), int(money_decimal))
        raise ValueError("a negative result is not allowed")


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

    e1 = Money(15, 95)
    e2 = Money(15, 95)

    e3 = e1 + e2
    print(e3)
    
    e4 = Money(15, 95)
    e5 = Money(1, 55)

    e6 = e4 - e5
    print(e6)