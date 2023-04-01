import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())

    if N**2 < M:
        print(-1)
        exit()
    # a < b として考える
    # aを固定して考える
    T = list(range(1, min(N+1, 10**6+1)))
    len_T = len(T)
    ans = 10**12+1
    for a in range(1, min(N+1, 10**6+1)):
        K = M // a
        index = bisect.bisect_left(T, M/a)
        if index == len_T:
            continue
        else:
            ans = min(ans, a*T[index])

    if ans == 10**12+1:
        print(-1)
    else:
        print(ans)

