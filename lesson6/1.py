import sys
from memory_profiler import profile
import platform
import random

""" 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
    Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

    Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. 
    Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
"""


# ф-я посчета затрачиной памяти по элементам
def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

@profile # декоратор для подсчета затраченной памяти приложением    ПРИМЕР ВЫВОДА НИЖЕ"

# задание с первого урока "Написать программу, которая генерирует в указанных пользователем границах:"
def lesson6():
    def rand_number(): # целое число
        print('Генерация целых чисел в указанном диапозоне')
        a = int(input('Введите от: '))
        b = int(input('Введите до: '))
        rand_number = random.randrange(a, b) # целое число
        print(f'Результат = {rand_number}')
    def rand_number_v():  # вещественное число
        print('Генерация вещественных чисел в указанном диапозоне')
        a = int(input('Введите от: '))
        b = int(input('Введите до: '))
        rand_number_v = random.random() * (a - b) + b
        print(f'Результат = {rand_number_v}')
    def rand_symbol():
        abc_list = []
        for i in range(ord('A'), ord('z') + 1):
            abc_list.append(chr(i))
        print(f'Генерация смволов\n{abc_list[:26]}\n{abc_list[27:31]}\n{abc_list[32:]}')
        a = ord(input('Ведите символ с клавиатуры для устанвки диапозона "от": '))
        b = ord(input('Ведите символ с клавиатуры для устанвки диапозона "до": '))
        rand_symbol =random.randrange(a, b)
        print(f'случайно выбранное число: {rand_symbol} в заданном диапозоне от {a} и до {b} соответствует символу "{chr(rand_symbol)}"')

    print('\n', 'Генерация в указанных пользователем границах:\n- случайное целое число = 1\n- случайное вещественное число = 2\n- случайный символ = 3')
    key = input('Укажите ключ: ')
    if key == '1':
        rand_number()
    elif key == '2':
        rand_number_v()
    elif key == '3':
        rand_symbol()
    else:
        print('Ой ой, что то пошло не так! ')

lesson6()
# вывод с профайла
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     15.3 MiB     15.3 MiB           1   @profile
    26                                         def lesso6():
    27     15.3 MiB      0.0 MiB           2       def rand_number(): # целое число
    28     15.3 MiB      0.0 MiB           1           print('Генерация целых чисел в указанном диапозоне')
    29     15.3 MiB      0.0 MiB           1           a = int(input('Введите от: '))
    30     15.3 MiB      0.0 MiB           1           b = int(input('Введите до: '))
    31     15.3 MiB      0.0 MiB           1           rand_number = random.randrange(a, b) # целое число
    32     15.3 MiB      0.0 MiB           1           print(f'Результат = {rand_number}')
    33     15.3 MiB      0.0 MiB           1       def rand_number_v():  # вещественное число
    34                                                 print('Генерация вещественных чисел в указанном диапозоне')
    35                                                 a = int(input('Введите от: '))
    36                                                 b = int(input('Введите до: '))
    37                                                 rand_number_v = random.random() * (a - b) + b
    38                                                 print(f'Результат = {rand_number_v}')
    39     15.3 MiB      0.0 MiB           1       def rand_symbol():
    40                                                 abc_list = []
    41                                                 for i in range(ord('A'), ord('z') + 1):
    42                                                     abc_list.append(chr(i))
    43                                                 print(f'Генерация смволов\n{abc_list[:26]}\n{abc_list[27:31]}\n{abc_list[32:]}')
    44                                                 a = ord(input('Ведите символ с клавиатуры для устанвки диапозона "от": '))
    45                                                 b = ord(input('Ведите символ с клавиатуры для устанвки диапозона "до": '))
    46                                                 rand_symbol =random.randrange(a, b)
    47                                                 print(f'случайно выбранное число: {rand_symbol} в заданном диапозоне от {a} и до {b} соответствует символу "{chr(rand_symbol)}"')
    48                                         
    49     15.3 MiB      0.0 MiB           1       print('\n', 'Генерация в указанных пользователем границах:\n- случайное целое число = 1\n- случайное вещественное число = 2\n- случайный символ = 3')
    50     15.3 MiB      0.0 MiB           1       key = input('Укажите ключ: ')
    51     15.3 MiB      0.0 MiB           1       if key == '1':
    52     15.3 MiB      0.0 MiB           1           rand_number()
    53                                             elif key == '2':
    54                                                 rand_number_v()
    55                                             elif key == '3':
    56                                                 rand_symbol()
    57                                             else:
    58                                                 print('Ой ой, что то пошло не так! ')

"""




num = [3, 5, 6, 34, 5, 1, 9, 5, 1, 34, 4, 8]

print(show_sizeof(num)) # тут берем вес каждого элемента в списке
# <class 'list'> 152 [3, 5, 6, 34, 5, 1, 9, 5, 1, 34, 4, 8]
# 	 <class 'int'> 28 3
# 	 <class 'int'> 28 5
# 	 <class 'int'> 28 6
# 	 <class 'int'> 28 34
# 	 <class 'int'> 28 5
# 	 <class 'int'> 28 1
# 	 <class 'int'> 28 9
# 	 <class 'int'> 28 5
# 	 <class 'int'> 28 1
# 	 <class 'int'> 28 34
# 	 <class 'int'> 28 4
# 	 <class 'int'> 28 8
# None


print(sys.getsizeof(num)) # тут смотрим общий вес переменной которой присвоин список

# 152




print(sys.platform)
print(f'Версия Python: {sys.hexversion}')
print(f'Версия Python: {sys.version}')
print(platform.platform())

# darwin
# Версия Python: 50987248
# Версия Python: 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)]
# macOS-11.6.1-x86_64-i386-64bit

