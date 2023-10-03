

if __name__ == '__main__':
    A, B = map(int, input().split())
    d = dict()
    d[1] = {2}
    d[2] = {1, 3}
    d[3] = {2}
    d[4] = {5}
    d[5] = {4, 6}
    d[6] = {5}
    d[7] = {8}
    d[8] = {7, 9}
    d[9] = {8}

    if A in d[B]:
        print('Yes')
    else:
        print('No')


