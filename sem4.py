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
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 