field = [[" "] * 3 for i in range(3)]
def show():
    print(f"   | 0 | 1 | 2 |")
    print("----------------")
    for i in range(3):
        row =f" {i} | {' | '.join(field[i])} |"
        print(f"{row} ")
        print("----------------")

def move():
    while True:
        print("")
        cords =  input("        Введите координаты : ").split()
        print("")

        if len(cords) != 2:
            print("Нужны 2 координаты")
            continue

        x, y = cords

        if not (x.isdigit) or  not (y.isdigit):
            print("Координаты должны быть чистами")
            continue

        x , y =int(x) , int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Клетка вне диапозона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True


    return False


num = 0
while True:
    num +=1

    show()

    if num % 2 ==1:
        print("_--_--_ Ходит крестик _--_--_")
    else:
        print("_--_--_ Ходит нолик _--_--_")

    x, y = move()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if num == 9:
        print("Ничья")
        break



