def check(a, b, c):
    ab = [b[0]-a[0], b[1]-a[1]]
    ac = [c[0]-a[0], c[1]-a[1]]

    if ab[0] == 0 or ac[0] == 0:
        if ab[0] == 0 and ac[0] == 0:
            return False
        else:
            return True

    if ab[1] == 0 or ac[1] == 0:
        if ab[1] == 0 and ac[1] == 0:
            return False
        else:
            return True

    if ab[0]/ac[0] == ab[1]/ac[1]:
        return False
    else:
        return True


if __name__ == '__main__':
    N = int(input())
    P = []
    for _ in range(N):
        pos = list(map(int, input().split()))
        P.append(pos)

    '''
    考察
    ・3点が１直線上にないような組み合わせ総数を求める
    ・Nは300個までなので、全通りで27*10**6でちょっと多い
    ・
    '''
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if check(P[i], P[j], P[k]):
                    ans += 1

    print(ans)




