# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# Импорт функции

import random
import os
os.system("cls")

# Введение данных

num_quantity = int(input('Введите размер списка: '))
# Создание пустого списка--------------------
array = []
# Функция заполнение пустого списка случайными числами-------------------- 
def array_filling(array, num_quantity):
    for i in range(1, num_quantity+1):
        random_num = random.randint(1, 50)
        array.append(random_num)
res_array = array_filling(array, num_quantity)
print(array)
# Ввод числа-ориентира для поиска ближайшего-------------------- 
closest_num_search = int(input('Введите число для поиска ближайшего по значению имеющегося в списке: '))
# Функция сортировки списка, перевод списка во множество и сравнение числа ориентира с полученным множеством--------------------
def array_sort(array, closest_num_search):
    array.sort()
    print(array)  
    new_set = set(array)
    min = 0
    max = 0
    for i in new_set:
        if i == closest_num_search:
            print(f'Число {closest_num_search} равно введенному {closest_num_search}.')
            # break
        else:
            if i < closest_num_search:
                min = i
            elif i > closest_num_search:
                max = i
                if closest_num_search - min > max - closest_num_search:
                    print(f'Ближайшее число для {closest_num_search} это число {max}.')
                    break
                elif closest_num_search - min < max - closest_num_search:
                    print(f'Ближайшее число для {closest_num_search} это число {min}.')
                    break
                elif closest_num_search - min == max - closest_num_search:
                    print(f'Числа {min} и {max} одинаково близки {closest_num_search}.')
                    break    
sort = array_sort(array, closest_num_search)