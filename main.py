def fillArr(size):
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

sizeA: int = 10
fillArr(sizeA)
print("\tStart\n\t\tGame \"Serpentine\"")
print("\t\tmatrix size {} x {}".format(sizeA, sizeA))