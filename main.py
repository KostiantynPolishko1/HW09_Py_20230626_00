import random

def print_arr(arr):
    for i in range(sizeA):
        if i == 0:
            print(" ", end='\t')
        elif i == sizeA - 1:
            print("(Y)", end='\t')
        else:
            print((sizeA - 1) - i, end='\t')
        for j in range(sizeA):
            print(arr[i][j], end='  ')
        print()
        if i == sizeA - 1:
            print("   ", end='')
            for n in range(sizeA - 1):
                if n == 0:
                    print("(X) ", end='')
                else:
                    print(n, end='  ')
            print()

def fill_arr(arr, size):
    for i in range(size):
        temp = []
        if i == 0 or i == size - 1:
            for j in range(size):
                temp.append("*")
        else:
            for j in range(size):
                if j == 0 or j == size - 1:
                    temp.append("*")
                else:
                    temp.append(" ")
        arr.append(temp)
    arr[1][1] = '@'

    return arr

def fill_enemy(arr):
    x2: int # enemies coordinates
    y2: int # enemies coordinates

    while True:
        y2 = random.randrange(1, 8)
        x2 = random.randrange(1, 8)
        if arr[y2][x2] == '@' or arr[y2][x2] == '+':
            continue
        else:
            arr[x2][y2] = '+'
            break
    return arr

def pos_player(arr, size):
    x_player, y_player = 0, 0  # player temporary coordinates
    for i in range(size):
        for j in range(size):
            if arr[i][j] == '@':
                x_player = i
                y_player = j

                return x_player, y_player

def check_new_pos_player(x_new, y_new, arr_check, size_arr):
    x_temp, y_temp = pos_player(arr_check, size_arr)  # function in order to receive current x, y coordinates of player

    if x_new > 9 or y_new > 9 or arr_check[x_new][y_new] == '*' or arr_check[x_new][y_new] == 'o':
        # move_num -= 1
        # ind_move_n += 1
        return True
    elif x_new != x_temp and y_new != y_temp:
        # move_num -= 1
        # ind_move_n += 1
        return True

    # fill track of player
    arr_check[x_temp][y_temp] = 'o'

    for i2 in range(x_temp, x_new, (1 if x_temp < x_new else -1)):
        arr_check[i2][y_new] = 'o'

    for j2 in range(y_temp, y_new, (1 if y_temp < y_new else -1)):
        arr_check[x_new][j2] = 'o'

def move_player(arr, size):

    print("\nPlayer, move in orthogonal:")
    while True:

        y = abs(float(input("\t\tenter pos x -> ")))
        x = abs(float(input("\t\tenter pos y -> ")))
        print()
        x = int(x)
        y = int(y)
        x = (sizeA - 1) - x

        if check_new_pos_player(x, y, arr, size): # function
            print("ERROR! pos x, y is uncorrect")
            continue

        arr[x][y] = '@'

        return arr
#--------------------------------------------------------#
sizeA: int = 10  # size of field game
arr_game = []
fill_arr(arr_game, sizeA)

print("\tStart\n\t\tGame \"Serpentine\"")
print("\t\tmatrix size {} x {}".format(sizeA, sizeA))

while True:
    fill_enemy(arr_game)
    print_arr(arr_game)

    while True:
        move_player(arr_game, sizeA)
        print_arr(arr_game)

        val = input("enter 1 - continue: ")
        if val == '1':
            continue
        else:
            break