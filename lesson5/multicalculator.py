from calculator import Calculator

class MultiCalcaulator(Calculator):
    numbers = []

    def __init__(self, *args):
        Calculator.__init__(self)
        for argument in args:
            self.numbers.append(argument)


    def __str__(self):
        self.numbers
        return str(self.numbers)

    def sum(self):
        sum = 0

        for num in self.numbers:
            sum += num

            return sum

    def difference(self):
        result = self.numbers[0]

        for num in self.numbers[1:]:
            result -= num

            return result

    def multiply(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result *= num

            return result

    def divide(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result /= num
            return result