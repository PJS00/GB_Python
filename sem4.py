# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split(

# 1. преобразуем в список, потому что строка - неизменяемая структура данных, а в списке элементы можно менять
# 2. создаем словарь
# 3. перебираем значения

# st = 'a a a b c a a d c d d'
# # st1 = st.split(' ')
# # from collections import Counter
# # cnt = dict(Counter(st))

# def ShowNewList(input_str):
#     """Здесь могут быть ваши комментарии. Функция замены значения списка."""
#     letters = input_str.split()

#     dict_1 = {}

#     for i in range(len(letters)):
#         if letters[i] not in dict_1:
#             dict_1[letters[i]] = -1 # чтобы нумерация повторяющихся элементов началась со второго элемента
#         dict_1[letters[i]] += 1 # если элемент существует, то к нумерации прибавляется 1

#         if dict_1[letters[i]] == 0:
#             continue # переход на следующий шаг цикла
#         letters[i] = letters[i] + "_" + str(dict_1[letters[i]])

#     print(letters)

# ShowNewList(st)

#  код с семинара
# dict = {}
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split():
#     count = dict.get(i)
#     if count != None:
#         string_res = string_res + i + "_" + str(count) + " "
#         dict[i] = count + 1
#     else:
#         dict[i] = 1
#         string_res = string_res + i + " "

# print(string_res)

# Не работет
# chg_st = [st1.replace(key, value)
#           for value in st1
#           for key, value in cnt.items()
#           if key in value]
# print(chg_st)
# for key in st1:
#     print(cnt[key].pop(0), end='')


# пример работы со строками, заменой символов
# st = '8 7 6 f 0 s'
# print(st)
# st = st.replace(" ", '').split(' ')
# print(st)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# input_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

#  оптимизированный код
# # words_num = len(set(input_str.replace(".", ' ').lower().split(" ")))
# # print(words_num)

# words_num = input_str.replace(".", ' ').lower().split(" ")
# def CntWord(user_list):
#     count = 0
#     dict1 = set()
#     for word in user_list:
#         if word not in dict1:
#             dict1.add(word)
#             count += 1
#     return count

# print(CntWord(words_num))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#     max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 

# num = int(input())
# max_num = num
# while num != 0:
#     if num > max_num:
#         max_num = num
#     num = int(input())
# print(max_num)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input('Введите количество чисел первого множества: '))
# m = int(input('Введите количество чисел второго множества: '))
# data_n = []
# data_m = []
# for i in range(n):
#     data_n.append(int(input('Введите число первого множества № {}: '.format(i + 1))))
# num = data_n[0]

# for i in range(m):
#     data_m.append(int(input('Введите число второго множества № {}: '.format(i + 1))))
# num = data_m[0]

# data_n = set(data_n)
# data_m = set(data_m)

# data_m_n = data_n.intersection(data_m)
# print(data_m_n)



# data_n = '2 4 6 8 10 12 10 8 6 4 2'
# data_m = '3 6 9 12 15 18'
# data_n = set(data_n.split())
# data_m = set(data_m.split())

# data_m_n = data_n.intersection(data_m)
# print(data_m_n)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# неверно
# arr = '1 2 3 4'
# arr = arr.split()
# i = 0
# sum = 0
# for i in range(len(arr)-1):
#     if (arr[i-1] + arr[i] + arr[i+1]) > sum:
#         sum = arr[i-1] + arr[i] + arr[i+1]
# print(sum)