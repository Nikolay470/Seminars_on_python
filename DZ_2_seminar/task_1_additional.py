# задача 1 сложная необязательная 
# Посчитать сумму цифр любого целого или вещественного числа. 
# Через строку решать нельзя.

n = 0.3546

while n % 1 != 0:
    n = n * 10

sum = 0
while(n != 0):
    sum = sum + (n % 10)
    n = n // 10

print(int(sum))