# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same

# def same_by(characteristic, objects):
#     # if len(objects) == 0:
#     #     return True
#     # for i in range(len(objects) - 1):
#     #     if characteristic(objects[i]) != characteristic(objects[i + 1]):
#     #         return False
#     # return True
#     return all(map(characteristic, objects)) # либо эта строчка
#     # return len(list(filter(characteristic, objects))) == len(objects) # либо эта, решение с семинара

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')



# st = '8 5 77 -14 101 45'
# Вывести двухзначные числа



# Напишите программу, которая подсчитает и выведет сумму
# квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# st = '9 1 2 -3 6 9'
# print(sum(map(lambda x: int(x) ** 2, filter(lambda a: int(a) % 9 == 0, st.split()))))