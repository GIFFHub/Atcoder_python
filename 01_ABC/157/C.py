

if __name__ == '__main__':
    N, M = map(int, input().split())
    ans = [-1]*N
    flg = True
    d = dict
    for _ in range(M):
        s, c = map(int, input().split())
        if s == 1 and c == 0 and N > 1:
            flg = False
        if ans[s-1] != -1:
            if ans[s-1] != c:
                flg = False
        ans[s-1] = c

    if flg:
        if ans[0] == -1:
            if N == 1:
                ans[0] = 0
            else:
                ans[0] = 1
        for i in range(1, N):
            if ans[i] == -1:
                ans[i] = 0
        tmp = 0
        cnt = 1
        for i, a in enumerate(reversed(ans)):
            tmp += a*cnt
            cnt *= 10
        print(tmp)
    else:
        print(-1)

