
def greet(): # приветствие
    print("-------------------")
    print("  Приветствуем Вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show(): # определяем функцию show, которая будет выводить игровое поле
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask(): # определяем функцию запроса от пользователя

    while True:
        cords = input("Ваш ход:     ").split() # переменная cords сохраняет оба значения

        if len(cords) != 2: # если длина списка не равно "2" повторяем ввод
            print('Введите 2 значения!')
            continue

        x, y = cords #присваеваем переменным x и y значения переменной cords(множественное присваивание)

        if not (x.isdigit()) or not (y.isdigit()): # если не является числом "x" или "y" запрос повторяется
            print('Введите числа!')
            continue

        x, y = int(x), int(y) # делаем строковые значения целочисленными

        if 0 > x or x > 2 or 0 > y or y > 2: # проверяем что введенные числа меньше 2 и больше 0
            print('Вводимые числа вне диапазона')
            continue

        if field[x][y] != ' ': # проверяем что поле пустое
            print('Клетка занята')
            continue

        return x, y


def check_win(): #определяем функцию условий победы
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord: # спомощью цикла перебираем значения и добавляем их в список для сравнения
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']: # если значение совпадает возвращается True и цикл завершается
            print('Выйграл X!!!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выйграл 0!!!')
            return True
    return False

greet()
field = [[' '] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if count == 9:
        print('Ничья!')
        break
