# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def arethmetic_progression(count_elem, f_elem, diff):
    res = [f_elem]
    for i in range(count_elem - 1):
        res.append(res[i] + diff)
    return res




quant_items = int(input("введите колличество элементов последовательности: "))
first_item = int(input("введите первый элемент последовательности: "))
difference = int(input("введите разность между элементами (числом): "))

result = arethmetic_progression(quant_items, first_item, difference)
print(result)