# 1.

from sys import argv

script_name = argv


def salary():
    work_time = int(input('Выработка в часах: '))
    rate = int(input('Ставка в рублях: '))
    prize = int(input('Премия в рублях: '))
    result = (work_time * rate) + prize
    print(f'Зароботная плата: {result} рублей')


salary()
