# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

number_N = int(input("введите ваше число: "))
degree_two = 1
number_two = 2
sum = 1

while sum < number_N:
    print(sum, end="; ")
    sum = 1
    for i in range(degree_two):
        sum = sum * number_two
    degree_two += 1    
