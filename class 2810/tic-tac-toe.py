# 2 players
d = 3


x_turn = True
turns_made = 0
field = []
for i in range(d):
    field.append([""]*d)
# ""- своюодно, "X" - крестик ,"O" - нолик
def print_field() -> None:
    global field
    for i in field:
       for j in i :
           if j =="":
               j = "_"
           print(j, end="")
       print()

def get_coords(name: str) -> [int, int]:
    correct = [str(i) for  i in range(1, d+1)]
    print("Ход " + name + ".введите номер строки от 1 до " + str(d))
    x = input(">")
    while x not in correct:
        print("Не коректно.введите номер строки от 1 до " + str(d))
        x = input(">")

    print(".введите номер столбца от 1 до " + str(d))
    y = input(">")
    while y not in correct:
        print("Не коректно.введите номер столбца от 1 до " + str(d))
        y = input()
    x = int(x) - 1
    y = int(y) - 1
    return [x, y]



def turn(x_turn: bool) -> None:
    global field
    if x_turn:
        name = "креcтиков"
        sym = "X"
    else:
        name = "ноликов"
        sym = "O"
    x, y = get_coords(name)
    while field[x][y] != "":
        print("ошибка.клетка занята" +field[x][y])
        x, y = get_coords(name)
    field[x][y] = sym

def check_win():
    out = ""
    global field
    for i in range(d):
        xs = field[i][0]
        ys = field[0][i]
        xwin, ywin = True, True
        for j in range(d):
            if field[i][j] != xs:
                xwin = False
            if field[j][i] != ys:
                ywin = False
        if not xwin and not ywin:
            out = ""
        if xwin and out == "":
            out = xs
        if ywin and out == "":
            out = ys
    xs = field[0][0]
    ys = field[0][d-1]
    xwin, ywin = True, True
    for i in range(d):

        if field[i][i] != xs:
            xwin = False
        if field[i][d-1-i] != ys:
            ywin = False
    if xwin and out == "":
        out = xs
    if ywin and out == "":
        out = ys
    return out

def reset() -> None:
    global field, x_turn, turns_made
    print("хотите продолжить? [да\нет]")
    s = input(">")
    if s == "нет":
        exit()
    field = []
    for i in range(d):
        field.append([""] * d)
    x_turn = True
    turns_made = 0
while True:
    print_field()
    turn(x_turn)
    x_turn = not x_turn
    result = check_win()
    if result == "":
        if turns_made >= d*d:
            print_field()
            print("ничья")
            reset()
    elif result == "X"  :
        print_field()
        print("победа крестиков ")
        reset()

    else:
        print_field()
        print("победа ноликов")
        reset()
