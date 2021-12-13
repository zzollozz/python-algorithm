a = 0
""" 1. Определение количества различных подстрок с использованием хэш-функции.
    Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
    Требуется найти количество различных подстрок в этой строке. """

import hashlib


def task1():
    string = input('Введите строку, состоящую только из маленьких латинских букв: ')

    sum_substring = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    print(f'{len(sum_substring) - 1} различных подстрок в строке {string}')





""" 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана. """

import heapq
from collections import Counter, namedtuple


class Note(namedtuple("Node", ["left", "right"])): # класс Узел с гранями
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])): # класс Лист с символом который он хранит
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s): # метод Хаффмана
    h = []
    for ch, fred in Counter(s).items():
        h.append((fred, len(h), Leaf(ch)))
    heapq.heapify(h) # очередь с приоритетами
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Note(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input('Введите сроку для кодирования методом Хаффмана: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(encoded))  # длинa закодированной строки
    for ch in sorted(code):  # перебор символов для кодирования и вывод из кода
        print(f"{ch}:  {code[ch]}")
    print(encoded)  # готовый результат


if __name__ == '__main__':
    task1()
    main()
