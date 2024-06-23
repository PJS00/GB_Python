# Задача
# Факториал числа n через рекурсию

# def fac(n):
#     if n in [0, 1]:
#         return 1
#     return n * fac(n - 1)

# list_1 = []
# for i in range(1, 7):
#     list_1.append(fac(i))
# print(list_1)

# Задача №31. Общее обсуждение
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Задача №37. Решение в группах
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы
# и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

def reverse(n):
    if n <= 0:
        return '->'
    num = input('Введи число: ')
    return reverse(n-1) + ' ' + num
print(reverse(4))

