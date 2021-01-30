import json


# 1.

with open('Task1.txt', 'w') as my_file1:
    str_my_file1 = input('Ведите что-нибудь: ')
    while str_my_file1:
        my_file1.writelines(str_my_file1)
        str_my_file1 = input('Ведите что-нибудь: ')
        if not str_my_file1:
            break
my_file1.close()

# 2.

with open(r'Task2.txt', 'r') as my_file2:
    x = 0
    for line in my_file2:
        x += 1
        print(f'Строка - {x}, Количество слов - {len(line.split())}')
    print(f'Количество строк - {x}')
my_file2.close()

# 3.

with open('Task3.txt') as my_file3:
    name_list = []
    salary_list = []
    for i in my_file3:
        list_task3 = i.split()
        if int(list_task3[1]) < 20000:
            name_list.append(list_task3[0])
        salary_list.append(list_task3[1])
print(f'Работники с окладом менее 20000: {name_list}\n '
      f'Средний оклад всех сотруников: {(sum(map(int, salary_list))) / len(salary_list):.2f}')
my_file3.close()

# 4.

with open('Task4.0.txt', 'r') as my_file4:
    task4_rus_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    new_file = []
    for el in my_file4:
        el = el.split(' ', 1)
        new_file.append(task4_rus_dict[el[0]] + '  ' + el[1])
    print(new_file)
my_file4.close()
with open('Task4.1.txt', 'w') as my_file41:
    my_file41.writelines(new_file)
my_file41.close()

# 5.

with open('Task5.txt', 'w') as my_file5:
    my_file5.write(input('Введите числа через пробел: '))
my_file5.close()

with open('Task5.txt', 'r') as my_file51:
    for i in my_file51:
        task5_list = i.split()
print(f'Сумма чисел = {(sum(map(int, task5_list)))}')

# 6.

file6_dict = {}
with open('Task6.txt', 'r') as my_file6:
    for line in my_file6:
        subject, lecture, practice, lab = line.split()
        file6_dict[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предметам - \n {file6_dict}')

# 7.

profit_dict = {}
middle_profit_dict = {}
profit = 0
profit_middle = 0
i = 0
with open('Task7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit_dict[name] = int(earning) - int(damage)
        if profit_dict.setdefault(name) >= 0:
            profit = profit + profit_dict.setdefault(name)
            i += 1
    if i != 0:
        profit_middle = profit / i
        print(f'Прибыль средняя - {profit_middle:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    middle_profit_dict = {'средняя прибыль': round(profit_middle)}
    profit_dict.update(middle_profit_dict)
    print(f'Прибыль каждой компании - {profit_dict}')

with open('Task7.json', 'w') as write_js:
    json.dump(profit_dict, write_js)

    js_str = json.dumps(profit_dict)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
