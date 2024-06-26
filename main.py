# python3 -m venv .folder - создание виртуального окружения
# филиал Питона в папке с проектом
# python main.py - запуск файла main.py в терминале

#n = 5  # задаем значение с типом int

# n = 'kjks\'fdhkj' # задаем сначение с типом str
#\перед символом выводит его на печать
# print(type(n))


# комментирование - символ # перед строкой или """ перед и после кода
# print(5)
# print(5)

# """
# print(5, 8)
# print(5)
# print(5, 9)
# """


# a = 5
# b = 5.89
# c = 'hello'

# примеры вывод и форматирования кода
# print(a, ' - ', b, ' - ', c)
# print("f"{a} - {b} - {c}"")
# print("{} - {} - {}".format(a, b, c))

# print('Введите первое число: ')
# input  - введение данных типа str
# a = input()
# b = input('Введите второе число: ')
# print(a, ' + ', b, ' = ', a + b)
# в итоге сложит 2 строки 5 + 6 = 56

# c = 1
# print(c)
# print(type(c)) # вывод типа значения

# c = bool(c)
# print(c)
# print(type(c))

# Нужно понимать, какой тип данных можно переводить в другой.
# Строку в int нельзя перевести
# v = 'gsdd'
# v = int(v)

# print('Введите первое число: ')
# # чтобы перевести str в int укажем int перед input
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)

# Арифметические операции
# + - сложение
# - - вычитание
# * - умножение
# / - деление (по умолчанию в вещественных числах с остатком)
# % - остаток от деления
# // - целочисленное деление
# ** - возведение в степень

# Приоритет операций
# 1. Возведение в степень
# 2. Умножение
# 3. Деление
# 4. Целочисленное деление
# 5. Остаток от деления
# 6. Сложение
# 7. Вычитание

# Округление чисел
# a = 5.7867
# b = 6.345234
# print(round(a*b, 3))
# round(1.34534, 2) - функция округления, round(x, y), где x - число, y - количество знаков после запятой 

# в c# были инкременты и т.д. i++
# в Питоне
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter **5

# Логические операции
# > -больше
# >= -больше или равно
# < - меньше
# <= - меньше или равно
# == - равно (проверяет, равны ли числа)
# != - не равно (проверяет, не равны ли значения)
# not - не (отрицание)
# and - и (конъюкция)
# or - или (дизъюкция)

# a = 1 > 4
# print(a) # ответ false

# a = 1 < 4 and 5 > 2
# print(a) # ответ true

# a = 1 == 2
# print(a) # ответ false

# a = 1 != 2
# print(a) # ответ true

# a = 'qwe'
# b = 'qwe'
# print(a == b) # ответ true

# a = 1 < 3 < 5 < 10
# print(a) # ответ true

# Цикл if else, elif
# username = input('Введите имя: ')
# if username == 'Маша': # двоеточие
#     print('Ура, это же Маша!') # отствупы таб или 4 пробела
# elif username == 'Марина':
#     print('Я так ждала вам, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет,', username)

# Цикл while
# Цикл позволяет выполнить блок кода, пока условие является верным
# n = 423
# sum = 0
# while n > 0:
#     x = n % 10
#     sum = sum + x
#     n = n // 10
# print(sum)

# Цикл while else
# Блок else выполняется, уогда основное тело цикла перестает
# работать самостоятельно. А разве кто-то может прекратить работу
# цикла? Если вспомнить c#, то да и эта конструкция break.
# Break лучше не использовать
# i = 5
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# На замену break приходит метод флажка
# Нахождение минимального делитея
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# В питоне цикл for в основном используется для перебора значений
# for i in условия
# for i in 1, -2, 3, 14, 5:
#     print(i)

# Функция range()
# range выдает значения из диапазона с шагом 1
# Если указано только одно число - от 0 до заданного числа
# Если нужен другой шаг, третьим аргументом можно задать приращение
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# Можно использовать цикл for со строками, так как у строк есть
#     нумерация, такая е как и у массивов, начинается с 0.
# for i in 'qwerty':
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)
# ответ:
# q
# w
# e 
# r
# t 
# y

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
# ответ:
# *****
# *****
# *****
# *****
# *****

# text = 'Съешь ещё этих МяГкИх фрнцузских булок'
# print(len(text)) # функция len - длина строки
# print('ещё' in text) # проверяем есть ли слово в нашей строке
# print(text.lower()) # переводим в нижний регистр
# print(text.upper()) # переводим в верхний регистр
# print(text.replace('ещё','ЕЩЁ')) # заменяем сочетание символов в строке

# Как и в массивах, есть отрицательная индексация.
# Можно использовать срезы
# text = 'съешь ещё этих мягких фрнцузских булок'
# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-1]) # к, как в массивах, используем отрицательный индекс, с конца
# print(text[-5]) # б
# print(text[:]) # выводятся все символы: съешь ещё этих мягких фрнцузских булок
# print(text[:2]) # выводим элемент с 0 по 2й: съ
# print(text[len(text)-2]) # о
# # где начинаем:где заканчиваем:шаг
# print(text[2:9]) # со 2 по 9: ешь ещё
# print(text[6:-18]) # ещё этих мягки
# print(text[0:len(text):6]) # сеикнио
# print(text[::6]) # сеикнио
# text = text[2:9] + text[-5] + text[:2]
# print(text)