

if __name__ == '__main__':
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()

    point = [0]

    '''
    ・引き返すことはないため、右に動くと考えて良い
    ・1個目は一番左に置ける
    ・距離の間隔が広いところから置いていく
    
    '''
    T = []
    for i in range(1, M):
        T.append((X[i]-X[i-1], i))
    T.sort(reverse=True)

    if N > 1:
        for t in T:
            point.append(t[1])
            N -= 1
            if N == 1:
                break

    point.sort()

    ans = 0

    for j in range(len(point)-1):
        ans += X[point[j+1]-1]-X[point[j]]

    if point[-1] != M-1:
        ans += X[-1] - X[point[-1]]
    print(ans)



