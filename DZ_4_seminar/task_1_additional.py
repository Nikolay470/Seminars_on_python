# задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, 
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def convert_to_binary_number(num):
    res = ""
    remainder = 0
    while num > 0:
        remainder = num % 2
        res = str(remainder) + res
        num = num // 2
    return res

def convert_to_octal_number(num):
    res = ""
    remainder = 0
    while num > 0:
        remainder = num % 8
        res = str(remainder) + res
        num = num // 8
    return res



number = int(input("введите целое положительное число: "))

binary_number = convert_to_binary_number(number)
octal_number = convert_to_octal_number(number)

print(f"число {number} в двоичном представлении равно {binary_number}")
print(f"число {number} в восьмеричном представлении равно {octal_number}")

print()
print(bin(number))
print(oct(number))