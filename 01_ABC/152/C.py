

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    '''
    自分より左が全て自分より大きいものの個数
    '''
    T = [N+1]*N
    tmp = N+1
    for i, p in enumerate(P):
        tmp = min(tmp, p)
        T[i] = tmp

    ans = 0
    for p, t in zip(P, T):
        if p <= t:
            ans += 1
    print(ans)


