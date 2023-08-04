# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import randint

def search_index_in_range(arr, min_num, max_num):
    res = list()
    for i in range(len(arr)):
        if min_num < arr[i] < max_num:
            res.append(i)
    return res




sp = [randint(0, 1000) for i in range(10)]
print(sp)
min_number = int(input("введите минимальное значение диапозона: "))
max_number = int(input("введите максимальное значение диапозона: "))

result = search_index_in_range(sp, min_number, max_number)
print(result)