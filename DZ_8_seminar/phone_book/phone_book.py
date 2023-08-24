import sqlite3 as sq

connect = sq.connect("phone_book.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS phone_book(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               private_phone TEXT,  
               work_phone TEXT,
               birth_data TEXT
)""")

###########################################################################

def print_phone_book():
    cursor.execute("""SELECT * FROM phone_book""")
    result = cursor.fetchall()
    for row in result:
        print(f"\n{row[0]}. {row[1]}\nличный телефон: {row[2]}\n"
          + f"рабочий телефон: {row[3]}\nдата рождения: {row[4]}\n")


def create_contact(name_con):
    private_phone_contact = input("Введите личный телефон, если нет поставьте прочерк ('-')\n")
    work_phone_contact = input("Введите рабочий телефон, если нет поставьте прочерк ('-')\n")
    birth_day_contact = input("Введите дату рождения, если нет поставьте прочерк ('-')\n")

    data = (name_con, private_phone_contact, work_phone_contact, birth_day_contact)
    cursor.execute("""INSERT INTO phone_book (name, private_phone, work_phone, birth_data)
                   VALUES(?, ?, ?, ?)""", data)
    connect.commit()
    print("Контакт успешно создан!\n")


def search_contact(name_con):
    names = cursor.execute("""SELECT name FROM phone_book """).fetchall()
    temp_name = (name_con,)
    if temp_name in names:
        return True
    else: 
        return False


def print_contact(name_con):
    cursor.execute("""SELECT * FROM phone_book WHERE name = ?""", (name_con,))
    row = cursor.fetchone()
    print(f"\n{row[0]}. {row[1]}\nличный телефон: {row[2]}\n"
          + f"рабочий телефон: {row[3]}\nдата рождения: {row[4]}\n")



def change_name(n_name, old_name):
    data = (n_name, old_name)
    cursor.execute("""UPDATE phone_book set name = ? WHERE name = ?""", data)
    connect.commit()


def change_phone(category, name, new_phone):
    data = (new_phone, name)
    if category == "priv":
        cursor.execute("""UPDATE phone_book set private_phone = ? WHERE name = ?""", data)
    else:
        cursor.execute("""UPDATE phone_book set work_phone = ? WHERE name = ?""", data)
    connect.commit()


def change_birth_data(name, n_data):
    data = (n_data, name)
    cursor.execute("""UPDATE phone_book set birth_data = ? WHERE name = ?""", data)
    connect.commit()


def change_contact(name_con):
    while True:
        command = int(input("\n1) Имя 2) Личный телефон\n3) Рабочий телефон" 
                                        + " 4) Дата рождения (введите номер)\n"))
        if command == 1:
            new_name = input("Введите новое имя\n").capitalize()
            change_name(new_name, name_con)
            command = int(input("\n1) Продолжить изменения\n2) Сохранить изменения\n"))
            if command == 1:
                continue
            else:
                break
        elif command == 2 or command == 3:
            new_number_phone = input("Введите новый номер\n")
            if command == 2:
                change_phone("priv", name_con, new_number_phone)
            else:
                change_phone("work", name_con, new_number_phone)
            command = int(input("\n1) Продолжить изменения\n2) Сохранить изменения\n"))
            if command == 1:
                continue
            else:
                break
        else:
            new_data = input("Введите новую дату\n")
            change_birth_data(name_con, new_data)
            command = int(input("\n1) Продолжить изменения\n2) Сохранить изменения\n"))
            if command == 1:
                continue
            else:
                break
    print("Контакт успешно изменен!")



def delete_contact(name_con):
    cursor.execute("""DELETE FROM phone_book WHERE name = ?""", (name_con,))
    connect.commit()
    print("Контакт успешно удален!")
##################################################################




while True:
    command = int(input("\nВведите номер\n"
                        + "1) Посмотреть все контакты\n"
                        + "2) Найти контакт\n"
                        + "3) Добавить контакт\n"
                        + "4) Выйти из справочника\n"))
    if command == 1:
        print_phone_book()
        command = input("1) Выберите контакт (введите имя)\n"
                        + "2) Для возврата к меню введите 'меню'\n"
                        + "3) Для выхода введите 'выход'\n").capitalize()
        if command == "Меню":
            continue
        elif command == "Выход":
            break
        else:
            name = command
            print_contact(name)
            command = int(input("1) Изменить контакт 2) Удалить контакт\n"))
            if command == 1:
                change_contact(name)
                command = int(input("\n1)Вернутся к меню 2) Выйти из справочника\n"))

                if command == 1:
                    continue
                else:
                    break
            elif command == 2:
                delete_contact(name)
                continue
        
    elif command == 2:
        name = input("Введите имя\n").capitalize()
        if search_contact(name):
            print_contact(name)
            command = int(input("1) Изменить контакт 2) Удалить контакт 3) Вернутся к меню\n"))
            if command == 1:
                change_contact(name)
                command = int(input("1)Вернутся к меню 2) Выйти из справочника\n"))

                if command == 1:
                    continue
                else:
                    break
            elif command == 2:
                delete_contact(name)
                continue
            else:
                continue

        else:
            print("Такого контакта в списке нет!")
    elif command == 3:
        name_contact = input("Введите имя\n").capitalize()
        create_contact(name_contact)
        command = int(input("1) Изменить контакт\n2) Удалить контакт\n"
                            + "3) Вернутся к меню\n4) Выйти из справочника\n"))
        if command == 1:
            change_contact(name_contact)
            command = int(input("1)Вернутся к меню\n2) Выйти из справочника\n"))
            if command == 1:
                continue
            else:
                break
        elif command == 2:
            delete_contact(name_contact)
            continue
        elif command == 3:
            continue
        else:
            break
    elif command == 4:
        break
    else:
        print("Введите коректную команду")
        continue

cursor.close()
connect.close()