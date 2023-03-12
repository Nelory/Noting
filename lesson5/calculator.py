class Calculator:
    a = 0
    b = 0



    def __init__(self, a=0, b=0):
        self.a = 0
        self.b = 0

    def __str__(self,):
        self.a = 10
        self.b = 5

        return \
            f'a = {self.a}'\
            f'a + b = {self.sum()}'\
            f'a - b = {self.difference()}' \
            f'a * b = {self.multiply()}'\
            f'a / b = {self.divide()}'

    def sum(self):
        return self.a + self.b
    def difference(self):
        return self.a - self.b
    def multiply(self):
        return  self.a * self.b
    def divide(self):
        return  self.a / self.b