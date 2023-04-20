

if __name__ == '__main__':
    N, M = map(int, input().split())
    T = [0]*M
    for i in range(N):
        K = list(map(int, input().split()))
        for j in range(1, K[0]+1):
            T[K[j]-1] += 1

    ans = 0
    for t in T:
        if t == N:
            ans += 1

    print(ans)


