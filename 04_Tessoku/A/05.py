if __name__ == '__main__':

    N, K = map(int, input().split())
    ans = 0
    T = min(N, K)
    for i in range(1, T+1):
        for j in range(1, T+1):
            if 1 <= K-i-j <= N:
                ans += 1
    print(ans)