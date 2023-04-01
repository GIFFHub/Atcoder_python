import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())

    if N**2 < M:
        print(-1)
        exit()
    # a < b として考える
    # aを固定して考える
    ans = 10**24+1
    for a in range(1, min(N+1, 10**6+1)):
        if M % a == 0:
            b = M // a
        else:
            b = M // a + 1
        if b <= N:
            ans = min(ans, a*b)

    print(ans)

