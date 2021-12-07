import random
from memory_profiler import profile
import time

""" 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
    заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
    Сортировка должна быть реализована в виде функции.
    По возможности доработайте алгоритм (сделайте его умнее). """


def sort_puz(a):
    a = [random.randrange(-100, 100) for _ in range(a)]
    n = True
    while (n):
        n = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                n = True
    return a

start_time = time.time()
# print(sort_puz(10))
# print(f'{time.time() - start_time} : секунд')


# --- 0.0007863044738769531 seconds --- это с переменной
# --- 0.0008652210235595703 seconds ---  это просто с len(a)
# По большому особй разници нет но без доп переменной l = len(a) даже незначительно но выполняется быстрее
# тоже и с использованием @profile памяти больше используется если допольнительно указывать l = len(a)

""" 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
    заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы. """



import operator



def merge_sort(list_numbers, compare=operator.lt):
    if len(list_numbers) < 2:
        return list_numbers[:]
    else:
        middle = int(len(list_numbers) / 2)
        left = merge_sort(list_numbers[:middle], compare)
        right = merge_sort(list_numbers[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# a = [random.randrange(0, 50) for _ in range(10)]
# print(a)
# print(merge_sort(a))

print(merge_sort([random.randrange(0, 50) for _ in range(10)]))





"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
    Медианой называется элемент ряда, делящий его на две равные части: 
    в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
    Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
    который не рассматривался на уроках """


def median(for_a_number_series):
    a = [random.randrange(100) for _ in range(for_a_number_series)]
    if len(a) % 2 == 0:
        print(f'Количество чисел в ряду чётно: {a}')
        a = sorted(a)
        n = int(len(a) / 2)
        r = (a[n] + a[n - 1]) // 2
        print(f'Упорядоченный ряд чисел: {a}\nМедиана равна: {r}')
    else:
        print(f'Количество чисел в ряду нечётно: {a}')
        a = sorted(a)
        n = int(len(a) / 2)
        print(f'Упорядоченный ряд чисел: {a}\nМедиана равна: {a[n]}')


# median(11)



