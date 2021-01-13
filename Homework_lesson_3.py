# 1.

def division(first_arg, second_arg):
    if second_arg == 0:
        return print('Деление на ноль не возможно')
    else:
        return first_arg / second_arg


print(division(float(input('Введите первое число: ')), float(input('Введите второе число: '))))


# 2.

def questionnaire():
    options = {
        'Имя': '',
        'Фамилия': '',
        'Год рождения': '',
        'Город проживания': '',
        'Email': '',
        'Телефон': ''
    }
    for i in options.keys():
        param = input(f'Введите "{i}"')
        options[i] = str(param)
    return print(options)


questionnaire()


def questionnaire1(name, surname, year, city, email, tel):
    return print(f''
                 f'Имя: {name}, '
                 f'Фамилия: {surname}, '
                 f'Год рождения: {year}, '
                 f'Город проживания: {city}, '
                 f'Email: {email}, '
                 f'Телефон: {tel}')


questionnaire1(name=input('Имя:'),
              surname=input('Фамилия:'),
              year=input('Год рождения:'),
              city=input('Город проживания:'),
              email=input('Email:'),
              tel=input('Телефон:')
              )

# 3.


def my_func(first, second, third):
    my_list = [first, second, third]
    my_list.sort(reverse=True)
    return print(my_list[0] + my_list[1])


my_func(1, 15, 10)


# 4.

def my_func1(x, y):
    return print(x**y)


print(my_func1(float(input("Первое значение - ")), int(input("Второе значение - "))))


def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(my_func2(float(input("Первое значение - ")), int(input("Второе значение - "))))

# 5.


def sum_func():
    sum_result = 0
    exit_func = False

    while not exit_func:
        numbers = input('Введите числа через пробел. Или введите "Q" для выхода: ').upper().split()
        result = 0
        for i in range(len(numbers)):
            if numbers[i] == 'Q':
                print('Вы вышли.')
                exit_func = True
                break
            else:
                result = result + int(numbers[i])
        sum_result = sum_result + result
        print(f'Сумма чисел = {result}')
    print(f'Финальная сумма чисел = {sum_result}')


sum_func()

# 6.


def int_func():
    my_word = input('Введите предложение: ').title()
    return print(my_word)


int_func()
