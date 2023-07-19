# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

product_of_numbers = int(input("введите произведение чисел: "))
sum_of_numbers = int(input("введите сумму чисел: "))

first_number = sum_of_numbers / 2
second_number = first_number

if(first_number % 1 != 0):
    first_number = int(first_number)
    second_number = first_number + 1

while(first_number * second_number != product_of_numbers):
    first_number -= 1
    second_number += 1

print(f"числа которые загадал Петя это {first_number} и {second_number}")