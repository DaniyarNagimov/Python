from functools import reduce
from itertools import cycle
from itertools import count
from math import factorial

# 2.

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i+1] for i in range(0, len(my_list)-1) if my_list[i+1] > my_list[i]]

print(new_list)


# 3.

my_list1 = [i for i in range(20, 240) if i % 20 == 0]
print(my_list1)


# 4.

my_list2 = [2, 2, 2, 7, 23, 1, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list2 if my_list2.count(i) == 1]

print(new_list)


# 5.

my_list3 = [i for i in range(99, 1001) if i % 2 == 0]

print(reduce(lambda x, y: x * y, my_list3))


# 6.

num = int(input('Введите конечное число: '))
for i in count(int(input('Введите начальное число число: '))):
    if i > num:
        break
    else:
        print(i)

c = 0
for el in cycle(['Hello!', 123, True, False]):
    if c > 50:
        break
    print(el)
    c += 1


# 7.


def fact(n):
    for i in count(1, 1):
        yield factorial(i)
        if i == n:
            break


for el in fact(5):
    print(el)
