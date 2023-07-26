# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло a[i] ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. 
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.
def spisok_amounts(spisok):
    sp_sum = []
    sum = 0
    for i in range(len(spisok)):
        if i == 0:
            sum = spisok[-1] + spisok[i] + spisok[i + 1]
            sp_sum.append(sum)
        elif i == len(spisok) - 1:
            sum = spisok[i - 1] + spisok[i] + spisok[0]
            sp_sum.append(sum)
        else:
            sum = spisok[i - 1] + spisok[i] + spisok[i + 1]
            sp_sum.append(sum)
    return sp_sum

def max_quantity_berries(spisok):
    spisok_sum = spisok_amounts(spisok)
    max_sum = spisok_sum[0]
    for sum in spisok_sum:
        if sum > max_sum:
            max_sum = sum
    return max_sum
    

harvest_from_bush = input("введите урожайность кустов через пробел (числом): ").split()
harvest_from_bush = [int(item) for item in harvest_from_bush]

max_quant_berries = max_quantity_berries(harvest_from_bush)
print(f"максимальное число ягод за один проход => {max_quant_berries}")
