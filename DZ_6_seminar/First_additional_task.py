# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
from random import randint

def print_field(matr):
    for i in range(len(matr)):
        print("------------")
        for j in matr[i]:
            print(j, end=" | ")
        print()
        if i == len(matr) - 1:
            print("------------")
######################################

def move_user(coord, matr):
    if matr[coord[0]][coord[1]] == "-":
        matr[coord[0]][coord[1]] = "x"
    else:
        print("эта ячейка занята, выберите другую")
###############################################

def check_rows(matr):
    for item in matr:
        if item[0] == item[1] == item[2] == "x":
            return True
        if item[0] == item[1] == item[2] == "0":
            return True
    return False
#################################################

def check_columns(matr):
    for i in range(len(matr[0])):
        if matr[0][i] == matr[1][i] == matr[2][i] == "x":
            return True
        if matr[0][i] == matr[1][i] == matr[2][i] == "0":
            return True
    return False
###############################################

def check_diagonal(matr):
    for i in range(2):
        if i == 0:
            if matr[0][0] == matr[1][1] == matr[2][2] == "x":
                return True
            if matr[0][0] == matr[1][1] == matr[2][2] == "0":
                return True
        if i == 1:
            if matr[0][2] == matr[1][1] == matr[2][0] == "x":
                return True
            if matr[0][2] == matr[1][1] == matr[2][0] == "0":
                return True
        return False
##################################################

def check_field(matr):
    for item in matr:
        for n in item:
            if n == "-":
                return False
    return True
###################################################

def check_total(matr):
    res_rows = check_rows(matr)
    res_columns = check_columns(matr)
    res_diagonal = check_diagonal(matr)
    res_field = check_field(matr)

    if res_rows or res_columns or res_diagonal or res_field:
        return True
    return False
####################################################

def input_coord():
    row = int(input("введите номер строки (от 1 до 3): "))
    row -= 1
    column = int(input("введите номер столбца (от 1 до 3): "))
    column -= 1

    return [row, column]
#############################################################
def move_bot(matr):
    while True:
        coord = [randint(0, 2) for _ in range(2)]
        if matr[coord[0]][coord[1]] == "-":
            break
    matr[coord[0]][coord[1]] = "0"



field = [["-", "-", "-"], 
         ["-", "-", "-",], 
         ["-", "-", "-"]]

while True:
    user = input_coord()
    move_user(user, field)
    print_field(field)

    if check_total(field):
        print("Игра окончена! Поздравляю ты выиграл!")
        break
    
    move_bot(field)
    print_field(field)

    if check_total(field):
        print("Игра окончена! Победа за ботом)))")
        break