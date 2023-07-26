# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def search_general_items(plenty1, plenty2):
    result = []
    for item in plenty1:
        for elem in plenty2:
            if item == elem:
                result.append(item)
    return result


first_spisok = input("введите числа для первого списка (через пробел): ").split()
second_spisok = input("введите числа для второго списка (через пробел): ").split()

first_plenty = set([int(item) for item in first_spisok])
second_plenty = set([int(item) for item in second_spisok])

general_elements = search_general_items(first_plenty, second_plenty)
general_elements.sort()

print(*general_elements, sep = " ")

