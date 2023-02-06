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

num_quantity = int(input('Введите размер списка (для корректной работы требуется значение более 7!): '))
# Создание пустого списка--------------------
array = []

# Функция заполнение пустого списка случайными числами

def array_filling(array, num_quantity):
    for i in range(1, num_quantity+1):
        random_num = random.randint(1, 20)
        array.append(random_num)
res_array = array_filling(array, num_quantity)
# Вывод списка--------------------
print(f'Случайный список: {array}')

# Ввод числа-ориентира для поиска ближайшего
 
closest_num_search = int(input('Введите число для поиска ближайшего по значению имеющегося в списке: '))

# Сортировка списка (К СОЖАЛЕНИЮ КОРРЕКТНО РАБОТАЕТ СО СПИСКАМИ БОЛЬШЕ 7 ЭЛЕМЕНТОВ!!!)

for i in range(num_quantity-1):
    for j in range(num_quantity-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]            
# Создание из спписка множества--------------------
new_set = set(array)
# Создание из множества нового списка для возможности обращения к индексам!--------------------
array = list(new_set) 
# Функция поиска ближадйшего числа
def array_search(array, closest_num_search):
    biggest_num = array[-1]
    smallest_num = array[0]
    # Условие превышения сравниваемого элемента элементов в списке
    if closest_num_search < smallest_num:
        print(f'Ближайшее число для {closest_num_search} это число {smallest_num}.')
    elif biggest_num < closest_num_search:
        print(f'Ближайшее число для {closest_num_search} это число {biggest_num}.')
    else:   
        min = 0
        max = 0
        for i in array:
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
search = array_search(array, closest_num_search)