import time
from random import *


def preview_game():
    """ Функция выводит зитульник нашей игры"""
    print('-------------' + 'ДОБРО ПОЖАЛОВАТЬ В КОНСОЛЬНУЮ ВЕРСИЮ ИГРЫ WORDLE!!!' + '-------------')
    print()
    print(
        'ПРАВИЛА ИГРЫ :\n1)Если вы угдали слово,загадонное нами:ВЫ ВЫИГРАЛИ!!!\n2) Если вы угадали букву и её место '
        'в слове, то буква будет в "[]" скобках\n2) Если вы '
        'угадали букву, '
        'но не угадали её место в слове, то буква будет в "()" скобках\n3) Если вы не угадали ни одну букву в слове, '
        'то слово будет без изменений\n4) Если вы '
        'введёте слово которое не существует или его нет в нашем словаре, то вы увидете фразу:"ОУ! Такого слова нет '
        'в словаре игры!"\n   Также, вам будет предложено случайное слово из словоря игры.')
    print()
    print('-------------' + 'УДАЧИ ВАМ И ВЕСЁЛОГО ВРЕМЯ ПРОВОЖДЕНИЯ С WORDLE!!!' + '-------------')


def get_cnt_letters():
    """Функция получает цифру - кол-во букв в слове,осуществляет проверку числа"""
    print('Для того, чтобы начать выберете количество букв в словах!')
    cnt_letters = input('Введите цифру от 3 до 8:')
    while not cnt_letters.isdigit():
        cnt_letters = input('Введите цифру согласно условию:')
    cnt_letters = int(cnt_letters)
    while 3 > cnt_letters or cnt_letters > 8:
        try:
            cnt_letters = int(input('Введите цифру согласно условию:'))
        except ValueError:
            cnt_letters = input('Введите цифру согласно условию:')
            while not cnt_letters.isdigit():
                cnt_letters = input('Введите цифру согласно условию:')
            cnt_letters = int(cnt_letters)
    return cnt_letters


def get_main_word(count_letters: int):
    """Функция выбирает рандомное слово из словаря игры"""
    s = []
    with open('noun_Russian.txt', 'r', encoding='UTF-8') as file:
        s += file.read().split()
    dictionary_words = [x.upper() for x in s if len(x) == count_letters]
    main_word = choice(dictionary_words)
    return main_word.upper(), dictionary_words


def check_win(user_word: str, main_word: str):
    """Функция проверяет слово на выигрыш"""
    check_word = []
    mw = main_word
    if user_word == main_word:
        return 'ВЫ ВЫИГРАЛИ!!!'
    for x, y in zip(user_word, main_word):
        if x == y:
            check_word += [f'[{x}]']
            mw = mw.replace(y, '', 1)
        elif x in main_word and x in mw and user_word.rindex(x) != main_word.index(x):
            check_word += [f'({x})']
            mw = mw.replace(x, '', 1)
        else:
            check_word += [f' {x} ']
    return check_word


def get_user_word(count_letters: int, dictionary_words: list):
    """Функция проверяет введённое пользователем слово """
    word = input(f'Введите слово длинной {count_letters} букв:')
    while len(word) != count_letters or word.isdigit() or word.upper() not in dictionary_words:
        if len(word) != count_letters or word.isdigit():
            word = input(f'Введите слово длинной {count_letters} букв:')
        elif word.upper() not in dictionary_words:
            print('ОУ! Такого слова нет в словаре игры!')
            print(f'Попробуйте слово {choice(dictionary_words).upper()}!')
            word = input(f'Введите слово длинной {count_letters} букв:')
    return word.upper()


def table(n: int, words: list):
    """Функция вывода таблицы на экран"""
    k = 0
    for i in range(5):
        print('______' * n)
        print(*[f'| {words[k + x]}' for x in range(n)], '|', sep=' ')
        print('------' * n)
        k += n


def secundomer(f):
    def wrapper():
        a = time.time()
        f()
        b = time.time()
        print(f'Время: {round(b - a, 1)} сек')

    return wrapper


@secundomer
def main():
    """Функция процесса игры"""
    preview_game()
    n = get_cnt_letters()
    s = []
    main_word, dictionary = get_main_word(n)
    print(main_word)
    k = 4
    for x in range(5):
        user_word_current = get_user_word(n, dictionary)
        word_check = check_win(user_word_current, main_word)
        if word_check == 'ВЫ ВЫИГРАЛИ!!!':
            print('ВЫ ВЫИГРАЛИ!!!')
            break
        if x == 0:
            s += word_check + ['  '] * 4 * n
        elif x > 0:
            s = [x for x in s if x != '  ']
            s += word_check + ['  '] * k * n
        table(n, s)
        k -= 1
    print(main_word)


if __name__ == '__main__':
    main()
