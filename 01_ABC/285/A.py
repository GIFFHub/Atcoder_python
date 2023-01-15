

if __name__ == '__main__':
    T = list(map(int, input().split()))

    T.sort()

    if T[1] // 2 == T[0]:
        print('Yes')
    else:
        print('No')

