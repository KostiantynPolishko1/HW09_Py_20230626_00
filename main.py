def fill_arr(size):
    arr = []
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

    return arr

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

#--------------------------------------------------------#
sizeA: int = 10

print("\tStart\n\t\tGame \"Serpentine\"")
print("\t\tmatrix size {} x {}".format(sizeA, sizeA))

arr_game = fill_arr(sizeA)
print_arr(arr_game)
