if __name__ == '__main__':
    N, S, M, L = map(int, input().split())

    ans = 1000000000000000
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                tmg = 6*i + 8*j + 12*k
                if tmg < N:
                    continue
                else:
                    tmp_money = S*i + M*j + L*k
                    ans = min(ans, tmp_money)

    print(ans)
