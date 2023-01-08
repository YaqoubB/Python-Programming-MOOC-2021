# WRITE YOUR SOLUTION HERE:


class Car:
    def __init__(self, petrol = 60, odometer = 0):
        if petrol <= 60:
            self.__petrol = petrol
        if odometer >= 0:
            self.__odometer = odometer

    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, km:int):
        if self.__petrol >= km:
            self.__odometer += km
            self.__petrol -= km
        else:
            self.__odometer += self.__petrol
            self.__petrol = 0
    
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
        
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)