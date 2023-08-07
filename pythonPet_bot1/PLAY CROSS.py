import time

print("*" * 1, "Игра Крестики-нолики(размер поля 3х3,стандартное)", "*" * 1)
field = list(range(1, 10))


def d_field(field):
    """Создаёт поле и выводит его в консоль"""
    print("*************")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("*************")


def start_game(token):
    """принимает данные , которые ввёл игрок"""

    st = False
    while not st:
        player_ans = int(input("Куда поставим " + token + "? "))
        if 1 <= player_ans <= 9:
            if str(field[player_ans - 1]) not in "XO":
                field[player_ans - 1] = token
                st = True
            else:
                print("Эта позиция уже занята.")
        else:
            print("Некорректный ввод!!! Что бы походить нужно ввести число от 1 до 9.")


def win_or_not(field):
    """Функция проверяет выиграли мы или нет"""
    w_cd = ((0, 1, 2), (0, 3, 6), (3, 4, 5), (1, 4, 7), (2, 4, 6), (6, 7, 8), (0, 4, 8), (2, 5, 8))
    for x in w_cd:
        if field[x[0]] == field[x[1]] == field[x[2]]:
            return field[x[0]]
    return False


def game(field):
    """Функция процесса игры"""
    cnt = 0
    w = False
    while not w:
        d_field(field)
        if cnt % 2 == 0:
            start_game("X")
        else:
            start_game("O")
        cnt += 1
        if cnt > 4:
            tp = win_or_not(field)
            if tp:
                print(tp, "Вы выиграли!")
                w = True
                break
        if cnt == 9:
            print("Ничья!")
            break
    d_field(field)


a = time.time()
game(field)
b = time.time()
print(b - a)
input("Нажмите Enter для выхода")
