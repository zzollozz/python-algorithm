import timeit


def search_for_a_prime_number(n): # Функция поиска i-го простого числа
    result = []
    for num in range(2, n + 1):
        for el in range(2, num):
            if num % el == 0:
                break
        else:
            result.append(num)
    return result



# aaa = search_for_a_prime_number(120)
# print(aaa)

def search_for_a_prime_number_2(n):  # Функция поиска i-го простого числа
    a = [i for i in range(n + 1)]

    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a

# bbb = search_for_a_prime_number_2(120)
# print(bbb)

NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'search_for_a_prime_number({TEST_VALUE})', setup='from __main__ import search_for_a_prime_number', number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'search_for_a_prime_number_2({TEST_VALUE})', setup='from __main__ import search_for_a_prime_number_2', number=NUMBER_EXECUTIONS)

print(f'Первый код:{time1}\nВторой код:{time2}\nРазница: {round(time2 / time1, 2)} раз')


'''
Первый код:0.004713496004114859
Второй код:0.0003098920060438104
Разница: 0.07 раз
'''