class NotEnoughFuel(BaseException):
    def __init__(self, message=''):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message

class Car:
    fuel = 0
    rate = 0.1
    traveled = 0

    def __init__(self, fuel=0, rate=0.1):
        self.fuel = fuel
        self.rate = rate
        self.traveled = 0

    def __str__(self):
        return \
            f'{self.fuel=}\n' \
            f'{self.rate=}\n' \
            f'{self.traveled=}\n'

    def go(self, distance):
        fuel_needed = distance * self.rate

        if fuel_needed > self.fuel:
            raise NotEnoughFuel(' NO FUEL!')

        self.fuel -= fuel_needed
        self.traveled += distance



car1 = Car(40, 0.1)
print(car1)


while True:
    try:
        car1.go(300)
    except NotEnoughFuel:
        print('FUEL END')
        break
    else:
        print(car1)
