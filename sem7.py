# num = '2 4 6 8 4 1'.split()
# # num = num.split() # Ошибка!
# print(num)

# num1 = list(map(int, num))
# print(num1)

# num1 = list(map(lambda x:int(x), num))
# print(num1)

# num1 = list(map(lambda x:x*2, num1))
# print(num1)

# мы не вызываем функцию сами, функция map сама вызовет функция, мы ей говорим
# "примени этот инструмент к каждому элементу итерритруемого
# объекта" переберет каждый элемент
# lambda сама не вызывает функцию

# функция filter
# num1 = list(filter(lambda x:x%8==0, num1))
# print(num1)

# num1 = list(filter(lambda x:100, num1))
# print(num1)

# num1 = list(filter(int, num1))
# print(num1)


# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №47. Решение в группах
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#    print('ok')
# else:
#     print('fail')


# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# решение с семинара
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# sqare = [(i[0]*i[1]) for i in orbits if i[0]!=i[1]]
# max_orbits = [(i[0], i[1]) for i in orbits if i[0] == max(sqare) / i[1]]
# print(*max_orbits)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda x: x[0] * x[1]))

# print(*max(orbits, key=lambda x: x[0] * x[1]*(x[0] != x[1])))


# print([yes, no][x>10])


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам
# Домашнее задание

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = 'аеёиоуыэюя'

# def rhythm(stroka):
#     stroka = stroka.split()

#     if len(stroka) <= 1:
#         print('Количество фраз должно быть больше одной!')
#         return
    
#     current_phrase_syllables = 0
#     previous_phrase_syllables = 0

#     for char in stroka[0]:
#         if char in vowels:
#             previous_phrase_syllables += 1

#     for phrase in stroka: 
#         for char in phrase:
#             if char in vowels:
#                 current_phrase_syllables += 1
#         if current_phrase_syllables != previous_phrase_syllables:
#             print('Пам парам')
#             return
#         previous_phrase_syllables = current_phrase_syllables
#         current_phrase_syllables = 0

#     print('Парам пам-пам')


# rhythm(stroka)


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y)
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     if num_columns < 2 or num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
#     for row in range(1 , num_rows + 1):
#         list = []
#         for column in range(1, num_columns + 1):
#             list.append(operation(row, column))
#         print(*list)
# print_operation_table(lambda x, y: x * y, 6, 6)

# решение с семинара
# def print_operation_table(operation, num_rows=9, num_columns=9):
#     pritntedRows = 1
#     printedColumns = 1
#     if num_columns < 2 or num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
#     maxLongNum = len(str(operation(num_columns, num_rows)))
#     while pritntedRows <= num_rows:
#         while printedColumns <= num_columns:
#             if maxLongNum < len(str(operation(printedColumns, pritntedRows))):
#                 maxLongNum = len(str(operation(printedColumns, pritntedRows)))
#             printedColumns += 1
#         pritntedRows += 1
#         printedColumns = 1
    
#     pritntedRows = 0
#     printedColumns = 0
#     while pritntedRows <= num_rows:
#         row = []
#         while printedColumns <= num_columns:
#             if pritntedRows == 0:
#                 row.append(('{0: >' + f'{maxLongNum}' + '}').format(printedColumns))
#             elif printedColumns == 0:
#                 row.append(('{0: >' + f'{maxLongNum}' + '}').format(pritntedRows))
#             else:
#                 if maxLongNum > 1:
#                     numbOperation = operation(printedColumns, pritntedRows)
#                     row.append(('{0: >' + f'{maxLongNum}' + '}').format(numbOperation))
#                 else:
#                     row.append(str(operation(printedColumns, pritntedRows)))
#             printedColumns += 1
#         print(*row, sep=' ')
#         pritntedRows += 1
#         printedColumns = 0


# print_operation_table(lambda x, y: x / y, 4, 4)