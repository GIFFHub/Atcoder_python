

if __name__ == '__main__':
    N = int(input())
    X = []
    Y = []
    d_x = dict()
    d_y = dict()
    T_x = [[] for _ in range(N)]
    T_y = [[] for _ in range(N)]

    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

        if x in d_x:
            for d in d_x[x]:
                T_x[d].append(i)
                T_x[i].append(d)
            d_x[x].append(i)
        else:
            d_x[x] = [i]

        if y in d_y:
            for d in d_y[y]:
                T_y[d].append(i)
                T_y[i].append(d)
            d_y[y].append(i)

        else:
            d_y[y] = [i]



    '''
    ・長方形の条件
    　・底辺を形成する2点のYが同じ
    　・右辺を形成する2点のXが同じ
    　・左辺を形成する2点のXが同じ
    　・上辺を形成する2点のYが同じ
    '''

    print(d_x)
    print(d_y)
    print(T_x)
    print(T_y)

    for tx1 in T_x:
        for tx2 in tx1:

