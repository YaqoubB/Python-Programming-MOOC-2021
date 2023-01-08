# Write your solution here:

class LunchCard:
    def __init__(self, balance: float):
        if balance >= 0:
            self.balance = balance
        self.owner = "None"
        if balance == 20:
            self.owner = "Peter"
        elif balance == 30:
            self.owner = "Grace"



    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60
    
    def deposit_money(self, amount: int):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
            
        else:
            self.balance += amount
        

    def __str__(self):
        if self.owner == "None":
            return f"The balance is {self.balance:.1f} euros"
        else:
            return f"{self.owner}: The balance is {self.balance:.1f} euros"



peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(peters_card)
print(graces_card)
peters_card.deposit_money(20)
graces_card.eat_special()
print(peters_card)
print(graces_card)
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(peters_card)
print(graces_card)



