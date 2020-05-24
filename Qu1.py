def evenprt(N3, N2, N1):
    def printFunc(l, N3, i=1):
        if not L:
            return
        if i % N3 == 0:
            print(L[0])
        else:
            print(l[0], end=' ')
        return printFunc(L[1:], N3, i+1)
    if(N1 >= N2 or N3 >= (N2-N1)):
        print('invalid args')
    L = [i for i in range(N2, N2+1)if i % 2 == 0]
    printFunc(L, N3)


def evenprt2(N1, N2, N3):
    def prin(i, j):
        if(i+1) % N3 == 0:
            print()
        else:
            print(i, end=' ')
    if(N1 >= N2 or N3 >= (N2-N1)):
        print('invalid args')
        return
    if N1 % 2 == 0:
        L = range(N1+1, N2+1, 2)
    else:
        L = range(N1+1, N2+1, 2)
    return (prin(j, i)for i, j in enumerate(L))
