# Задание 1 необязательное Сделайте локальный чат-бот с внешним хранилищем. 
# Тема чат-бота - любая вам интересная.
import json

def print_sp_books(spisok):
    names_books = list(spisok.keys())
    for i in range(len(spisok)):
        print(f"{i + 1}) \"{names_books[i]}\" автор: {spisok[names_books[i]]}")

def print_book(name_book, name_author):
        print(f"Книга: {name_book}, автор: {name_author}\n"
                + "Описание:\n Сдесь краткое описание книги\n"
                + "1) Читать онлайн 2) Добавить в избраное 3) Поставить оценку 4) Вернуться к выбору")

def serch_book(list_genre):
        name_book_search = input("Введите название книги: ").capitalize()
        for item in list_genre:
            names_keys = list(item.keys())
            for name in names_keys:
                if name == name_book_search:
                    return [name, item[name]]
                else: 
                    return -1
                
def print_my_grades(grades):
    name_book = list(grades.keys())
    for i in range(len(grades)):
        print(f"\"{name_book[i]}\" - ваша оценка {grades[name_book[i]]}")

def print_favorites(favor):
    print("Вам понравились эти книги: \n ")
    for item in favor:
        print(f"\"{item[0]}\" автор: {item[1]}")

def save(arg):
    if arg == favorites:
        with open("favorites.json", "w", encoding="utf-8") as fav:
            fav.write(json.dumps(arg, ensure_ascii=False))
    else:
        with open("my_grades.json", "w", encoding="utf-8") as grad:
            grad.write(json.dumps(arg, ensure_ascii=False))
    
                
#############################################################################
sp_books_genre_adventures = {"В сердце Борнео": "Редмонд О’Хэнлон",
                             "Копи царя Соломона": "Генри Райдер Хаггард",
                             "Гора: мое время на Эвересте": "Эд Виестурс",
                             "Моби Дик": "Герман Мелвилл",}

sp_books_genre_fantastic = {"Вокруг света за 80 дней": "Жюль Верн",
                            "Война миров": "Герберт Уэллс",
                            "Человек-амфибия": "Александр Беляев",
                            "Академия": "Айзек Азимов"}

sp_books_genre_novel = {"Три мушкитёра": "А. Дюма",
                        "На западном фронте без перемен": "Эрих М. Ремарк",
                        "Преступление и наказание": "Ф. Достоевский",
                        "Унесенные ветром": "М. Митчелл"}

sp_books_genre_horror = {"Хребты безумия": "Говард Ф. Лавкрафт",
                         "Коллекционер": "Джон Фаулз",
                         "Призраки дома на холме": "Ширли Джексон",
                         "Таинственные истории": "Эдгар По"}

sp_books_genre_detective = {"Девушка с татуировкой дракона": "Стиг Ларссон",
                            "Дурная кровь": "Роберт Гэлбрейт",
                            "Тайное место": "Тана Френч",
                            "Безмолвный пациент": "Алекс Михаэлидис"}
sp_genre = [sp_books_genre_adventures, sp_books_genre_fantastic, sp_books_genre_novel,
            sp_books_genre_horror, sp_books_genre_detective]
favorites = list()
my_grades = dict()
###########################################################################



with open("favorites.json", "r", encoding="utf-8") as fav:
    favorites = json.load(fav)
with open("my_grades.json", "r", encoding="utf-8") as grad:
    my_grades = json.load(grad)

command = 0
while True:
    print()
    move = int(input("Привет, что ты хочешь сделать?\n"
                     + "1) Выбрать книгу 2) Поставить оценку 3) Найти книгу\n" 
                     +"4) Посмотреть избранное 5) Посмотреть мои оценки 6) Завершить (введите номер):\n"))
    print()
    if move == 1:
        # выбор жанра ################################################
        choice_genre = int(input("Я помогу тебе выбрать интересную книгу, " 
                                + "которая увлечет тебя до самого конца!\n"
                                + "Давай начнем с выбора жанра:\n"
                                + "1) приключениия 2)фантастика\n"
                                + "3) роман 4) ужасы 5) детектив (введите номер выбранного варианта): \n"))
        
        current_genre = sp_genre[choice_genre - 1]
        print("\nВот что я могу предложить: \n")
        print_sp_books(current_genre)

        # выбор книги ######################################
        choice_book = int(input("Что-нибудь заинтересовало? "
                            + "Смело вводите номер понравившейся книги!\n"))
        
        names_books = list(current_genre.keys())
        book = names_books[choice_book - 1]
        author = current_genre[book]

        print_book(book, author)
        command = int(input())
        if command == 1:
            print("Вы перешли к электронному варианту книги")
            break
        elif command == 2:
            favorites.append([book, author])
            save(favorites)
            command = int(input("Книга добавлена в избранное. "
                                + "Хотите продолжить выбор?\n"
                                + "1) Да 2) Нет, завершить.\n"))
            if command == 1:
                continue
            else:
                break
        elif command == 3:
            grade = int(input("Как вы оцениваете эту книгу (от 1 до 5):\n"))
            my_grades[book] = grade 
            save(my_grades)   
            command = int(input("Ваша оценка принята! Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору\n")) 
            if command == 1:
                break
            else:
                continue
        else:
            continue

    if move == 2:
        # поставить оценку ###########################################
        param_book = serch_book(sp_genre)
        grade = int(input("Как вы оцениваете эту книгу (от 1 до 5): \n"))
        my_grades[param_book[0]] = grade
        save(my_grades)
        command = int(input("Ваша оценка принята! Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору 3) Посмотреть мои оценки 4) Посмотреть избранное\n"))
        if command == 1:
            break
        elif command == 2:
            continue
        elif command == 3:
            print_my_grades(my_grades)
            print()
            command = int(input("Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору 3) Показать избранное\n"))
            if command == 1:
                break
            elif command == 2:
                continue
            else:
                print_favorites(favorites)
                command = int(input("Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору\n"))
                if command == 1:
                    break
                elif command == 2:
                    continue
        else:
            print_favorites(favorites)
            command = int(input("Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору 3) Показать мои оценки\n"))
            if command == 1:
                break
            elif command == 2:
                continue
            else:
                print_my_grades(my_grades)
                command = int(input("Что будем делать? \n"
                            + "1) Завершить 2) Вернуться к выбору\n"))
                if command == 1:
                    break
                elif command == 2:
                    continue

    if move == 3:
        # найти книгу ################################################################
        name_and_author = serch_book(sp_genre)
        if name_and_author == -1:
            print("К сожалению такой книги у меня нет :-(")
            command = int(input("Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
            if command == 1:
                break
            else: 
                continue
        else:
            print_book(name_and_author[0], name_and_author[1])
            command = int(input())
            if command == 1:
                print("Вы перешли к электронному варианту книги")
                break
            elif command == 2:
                favorites.append([name_and_author[0], name_and_author[1]])
                save(favorites)
                command = int(input("Книга добавлена в избранное. "
                                    + "Хотите продолжить выбор?\n"
                                    + "1) Да 2) Нет, завершить.\n"))
                if command == 1:
                    continue
                else:
                    break
            elif command == 3:
                grade = int(input("Как вы оцениваете эту книгу (от 1 до 5):\n"))
                my_grades[name_and_author[0]] = grade 
                save(my_grades)   
                command = int(input("Ваша оценка принята! Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
                if command == 1:
                    break
                else: 
                    continue
            else:
                continue
    
    if move == 4:
        # показать избранное ###################################################
        if len(favorites) == 0:
            print("Ваш список любимых книг пока пуст :-(") 
            command = int(input("Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
            if command == 1:
                break
            else: 
                continue
        else:    
            print_favorites(favorites)
            print()
            command = int(input("Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
            if command == 1:
                break
            else: 
                continue
    if move == 5:
        # показать оценки ##########################################################
        if len(my_grades) == 0:
            print("Вы пока что не оценивали книги")
            command = int(input("Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
            if command == 1:
                break
            else: 
                continue
        else:
            print_my_grades(my_grades)
            print()
            command = int(input("Что будем делать? \n"
                                + "1) Завершить 2) Вернуться к выбору\n"))
            if command == 1:
                break
            else: 
                continue
    if move == 6:
        break