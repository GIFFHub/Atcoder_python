

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))
    DP = [0 for _ in range(N)]
    for i in range(N):
        if i == 0:
            pass
        elif i == 1:
            DP[i] = abs(H[i]-H[i-1])
        else:
            DP[i] = min(DP[i-1]+abs(H[i]-H[i-1]), DP[i-2]+abs(H[i]-H[i-2]))

    print(DP[N-1])

