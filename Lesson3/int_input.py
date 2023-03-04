
def int_input(message=''):

    try:
        a = int(input(message))
    except ValueError:
        print('Введите Числовое значение!!!!!!!!!!!')
        a = int_input('Введите Число')
    else:
        pass
    finally:
        print(a)

    return a

a = int_input('Введите число')