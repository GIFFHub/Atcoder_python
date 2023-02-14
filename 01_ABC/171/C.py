import string

if __name__ == '__main__':
    N = int(input())
    alf = string.ascii_lowercase

    T = []
    while True:
        if N < 26:
            T.append(alf[N-1])
            break
        tmp = N % 26
        if tmp == 0:

        T.append(alf[tmp-1])
        N //= 26




    T.reverse()
    print(''.join(T))








