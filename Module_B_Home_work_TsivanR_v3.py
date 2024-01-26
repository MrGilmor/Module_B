# добавление библиотеки sys
import sys
# процесс авторизации из B5_5.4.15
# auth - проверка Y/N
# has_access - проверка на пользователя
def is_auth(func):
    def wrapper():
        if auth:
            print("Вход выполнен")
            func()
        else:
            print("Пользователь неавторизован. Запуск игры приостановлен")
    return wrapper
def has_access(func):
    def wrapper():
        if auth:
            if username in USERS:
                print(f"Авторизация прошла успешно. {username} вошел в игру")
                func()
            else:
                print("Доступ пользователю", username, "запрещен")
    return wrapper

# приветствие в игре и пояснение правил
def game_start():
    print("  ***Игра в крестики-нолики*** ")
    print("  ---------------------------  ")
    print("     Приветствую вас в игре!   ")
    print("  ---------------------------  ")
    print("  Для ввода необходимо задавать")
    print("  координату через x и y, где  ")
    print("  x - номер строки (A-B-C)     ")
    print("  y - номер столбца (1-2-3)    ")
    print("  ---------------------------  ")

# Создание игрового поля 3 на 3.
def field_create():
    print()
    print("    | 1 | 2 | 3 | ")
    print("---------------")
    for i, row in enumerate(game_field):
        row_change = f"  {' | '.join(row)} | "
        print(row_change)
        print("---------------")


# Основной код запроса к пользователю по вводу координат
def main_fn():
    while True:
        xy = input("          Ваш ход: ").split()

        if len(xy) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = xy

        if x not in horizontal:
            print("Введите значение только из ABC для x!")
            continue

        if not y.isdigit():
            print("Введите число для y!")
            continue

        x, y = horizontal.get(x), int(y)

        if x > 2 or x < 0 or y > 3 or y < 1:
            print("Вне диапазона!")
            continue

        if game_field[x][y] != "-":
            print(" Клетка занята! ")
            continue

        return x, y


# определяем выиграшную комбинацию. Перечисляем все строки, все столбцы
# все горизонтальные линии
# каждая комбинация описывается кортежем из 3 точек,
# каждая точка описывается кортежем из двух чисел
# дальше создаем пустой список и проходимся по точкам. Если все Х - выиграл Х и наоборот
def winner_check():
    win_xy = (((0, 1), (0, 2), (0, 3)), ((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)),
              ((0, 3), (1, 2), (2, 1)), ((0, 1), (1, 2), (2, 3)), ((0, 1), (1, 1), (2, 1)),
              ((0, 2), (1, 2), (2, 2)), ((0, 3), (1, 3), (2, 3)))
    for xy in win_xy:
        symbols = []
        for a in xy:
            symbols.append(game_field[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    return False

# -----------------------------------------------------
# основное тело кода, в котором вызываются все функции!
# -----------------------------------------------------
# предварительная проверка логина и юзера
USERS = ['admin', 'Roma', 'quest']
yesno = input("Вы хотите сыграть в игру? Y/N: ")
auth = yesno == "Y"
if auth:
    username = input("Введите ваш Username: ")

horizontal= {"A": 0, "B": 1, "C": 2}
game_field = [[i, "-", "-", "-"] for i in horizontal.keys()]

#game_field = [["-"] * 3 for i in range(3)] - В разборе указан такой код. Усовершенствовал и добавил ABC

# Начало игры
@is_auth
@has_access
def main_game_func():
    game_start()

    cnt = 0
    while True:
        if auth:
            if username in USERS:
                cnt += 1

                field_create()

                if cnt % 2 == 1:
                    print("Ходит <Х>!")
                else:
                    print("Ходит <0>!")

                x, y = main_fn()

                if cnt % 2 == 1:
                    game_field[x][y] = "X"
                else:
                    game_field[x][y] = "0"

                if winner_check():
                    break

                if cnt == 9:
                    print("Ничья!")
                    break
main_game_func()

def exit():
    e = input("Нажмите любую клавишу и enter для выхода!")
    if e:
        sys.exit()
    else:
        sys.exit()
exit()
