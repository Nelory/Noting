a = 6
b = 2

try:
    file = open('text.txt')
    print(f'{a} / {b} = {a / b}')

except ZeroDivisionError:
    print('делить на ноль нельзя!')
except NameError as error:
    print(f'Использовано несуществующее название: {error}')
except Exception as error:
    print(type (error), error)
except ValueError as error:
    print(f'Введите число: {error}')
else:
    print('Исключений не была!')
finally:
    print('dsfsf')

print('Конец программы')