
if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    T = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())

        T[a-1].append(b-1)
        T[b-1].append(a-1)
    #print(T)

    for t in T:
        len_t = len(t)
        print('%d ' % len_t, end='')
        if len_t == 0:
            print()
            continue
        t.sort()
        for i in range(len_t):
            t[i] += 1
            if i == 0:
                print('%d' % t[i], end='')
            else:
                print(' %d' % t[i], end='')
        print()




