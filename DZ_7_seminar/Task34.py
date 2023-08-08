# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*


# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def search_quant_vowels(poem, sp_letters):
    sp_words = list()
    quant_vowels = list()

    for item in poem:
        sp_words.append(item.split("-"))
    for elem in sp_words:
        count = 0
        for word in elem:
            for letter in sp_letters:
                for n in word:
                    if letter == n:
                        count += 1
        quant_vowels.append(count)
    return quant_vowels
############################################################

def is_rhythm(poem, sp_letters):
    count_vowels = search_quant_vowels(poem, sp_letters)
    
    for i in range(1, len(count_vowels)):
        if count_vowels[i] != count_vowels[i - 1]:
            return False
    return True




vowels_letters = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
phrases = input("введите стих: ").split(" ")

if is_rhythm(phrases,vowels_letters):
    print("ритм есть")
else:
    print("ритма нет")