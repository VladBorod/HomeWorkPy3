# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# Импорт функции

import random
import os
os.system("cls")
# Введение данных

num_quantity = int(input('Введите размер списка: '))
# Создание пустого массива--------------------
array = []
# Заполнение пустого массива случайными числами-------------------- 
for i in range(1, num_quantity+1):
    random_num = random.randint(1, 20)
    array.append(random_num)
print(array)
# Ввод искомого числа для подсчета-------------------- 
num_for_count = int(input('Введите искомое число, требующее подсчета: '))
# Функция подсчета искомого числа--------------------
def num_count (array, num_for_count):
    count = 0
    for i in array:
        if i == num_for_count:
            count += 1
    return count
result = num_count(array, num_for_count)
print(f'Искомое число {num_for_count} встречается в списке {result} раз(а).')


