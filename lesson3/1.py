import random
from unittest import case

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
def task_1():
    result = {}
    for a in range(2, 10):
        result[a] = []
        for b in range(2, 100):
            if b % a == 0:
                result[a].append(b)

    for i in result:
        print(result[i])

# task_1()

""" 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
    то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих 
     позициях первого массива стоят четные числа. """

def task_2():
    num = [(random.randrange(100)) for i in range(6)]
    print(num)
    print(f'индексы четных элементов первого массива: {[num.index(i) for i in num if i % 2 == 0]}')

# task_2()


""" 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """
def task_3():
    num = [(random.randrange(100)) for i in range(6)]
    print(num)
    a = min(num)
    b = max(num)
    c = num[num.index(a)]
    num[num.index(a)] = num[num.index(b)]
    num[num.index(b)] = c
    print(num)

# task_3()


""" 4. Определить, какое число в массиве встречается чаще всего. """

num = [3, 5, 6, 34, 5, 1, 9, 5, 1, 34, 4, 8]

def task4_1(list):
    return max(set(list), key = list.count)


# print(task4_1(num))

def task_4(list):
    counter = 0
    num = list[0]

    for i in set(list):
        a = list.count(i)
        if (a > counter):
            counter = a
            num = i

    return num


# print(task_4(num))




""" 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

num_list = [-10, 3, 5, 0, -2, 1, 8]

def task_5(list):
    result = []
    for i in list:
        if i < 0:
            result += [i]
    print(max(result))

# task_5(num_list)



""" 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать. """

nums = [3, 5, 6, 34, 5, 2, 9, 5, 1, 34, 4, 8]

# print(nums)

def task_6(num):
    a = min(num)
    b = max(num)

    if num.index(a) < num.index(b):
        d = num[num.index(a)+1:num.index(b)]
        print(max(d))
    else:
        d = num[num.index(b)+1:num.index(a)]
        print(f'сумму элементов, находящихся между минимальным и максимальным элементами = {sum(d)}')
        print(d)

# task_6(nums)




""" 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой 
    (оба являться минимальными), так и различаться. """

nums = [3, 5, 6, 34, 5, 2, 9, 5, 1, 34, 4, 8]

def task_7(num):
    _ = num
    print(_)
    a = min(_)
    _.remove(a)
    b = min(_)
    print(a, b)


# task_7(nums)




""" 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
    введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
    В конце следует вывести полученную матрицу."""




def matrix():
    matrix_list = [[(random.randrange(99)) for _ in range(4)] for i in range(4)] # создали матрицу

    matrix_max = [sum(l) for l in matrix_list] # сумма строк
    for z in range(4):
        matrix_list[z].append(matrix_max[z])

    for a in matrix_list: # вывод матрицы
        print(('{:>4d}' * 5).format(*a))

# matrix()


""" 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

def matrix_max():

    matrix_list = [[(random.randrange(99)) for _ in range(4)] for i in range(4)] # создали матрицу

    matrix_max = [sum(l) for l in matrix_list] # сумма строк
    for z in range(4):
        matrix_list[z].append(matrix_max[z])

    for a in matrix_list: # вывод матрицы
        print(('{:>4d}' * 5).format(*a))

    matrix_max2 = [[matrix_list[z][i] for z in range(4)] for i in range(4)]
    matrix_min = [min(l) for l in matrix_max2]
    print(('{:>4d}' * 4).format(*matrix_min))

    print(f'максимальный элемент среди минимальных элементов столбцов матрицы = {max(matrix_min)}')


# matrix_max()