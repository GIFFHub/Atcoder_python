

if __name__ == '__main__':
    N = int(input())

    while True:
        if N % 2 == 0:
            N //= 2
        elif N % 3 == 0:
            N //= 3
        else:
            break

    if N == 1:
        print('Yes')
    else:
        print('No')

