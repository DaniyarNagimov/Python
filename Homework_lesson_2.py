# 1.

my_list = ['ручка', 54557, 125.548, True, ['chek'], {'hello'}, {'cross': 2}]
i = 0
while i < len(my_list):
    print(type(my_list[i]))
    i += 1


# 2.

el_count = int(input("Введите количество элементов списка "))
my_list2 = []
i = 0
el = 0
while i < el_count:
    my_list2.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list2)/2)):
    my_list2[el], my_list2[el + 1] = my_list2[el + 1], my_list2[el]
    el += 2
print(my_list2)


# 3.

month = int(input('Введите месяц в числовом формате: '))

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

seasons_dict = {
    1: "Зима",
    2: "Весна",
    3: "Лето",
    4: "Осень",
}

if month <= 2 or month == 12:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif 3 <= month <= 5:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif 6 <= month <= 8:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif 9 <= month <= 11:
    print(seasons_list[3])
    print(seasons_dict.get(4))


# 4.

my_string = input('Введите предложение: ').split()

num = 0
for i in my_string:
    num += 1
    print(num, i[:10])


# 5.

nums_list = [7, 5, 3, 3, 2]
user_num = input('Введите число(stop - выход): ')
while user_num != 'stop':
    user_num = int(user_num)
    for i in range(len(nums_list)):
        if nums_list[i] == user_num:
            nums_list.insert(i + 1, user_num)
            break
        elif nums_list[i] < user_num:
            nums_list.insert(0, user_num)
            break
        elif nums_list[-1] > user_num:
            nums_list.append(user_num)
            break
        elif nums_list[i] > user_num > nums_list[i + 1]:
            nums_list.insert(i + 1, user_num)
            break
    print(f'Текущий рейтинг: {nums_list}')
    user_num = input('Введите число: ')


# 6.

my_tuple = []
options = {'Название': '', 'Цена': '', 'Количество': '', 'Ед': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед': []}
num = 0
feature = None
control = None
while True:
    control = input("Введите 'Q' чтобы выйти, что бы продолжить нажмите 'Enter', для вывода аналитики нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"*" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("*" * 30)
    for i in options.keys():
        feature = input(f'Введите "{i}"')
        options[i] = int(feature) if (i == 'price' or i == 'quantity') else feature
        analytics[i].append(options[i])
    my_tuple.append((num, options))
