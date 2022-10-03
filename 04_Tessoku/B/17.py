

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    # dp[i] : i個目の足場にたどり着く最小コスト

    dp = [None] * N

    dp[0] = 0
    dp[1] = abs(H[1]-H[0])

    for i in range(2, N):
        dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

    Place = N-1
    answer = []

    while True:
        answer.append(Place+1)
        if Place == 0:
            break
        if dp[Place-1]+abs(H[Place]-H[Place-1]) == dp[Place]:
            Place -= 1
        else:
            Place -= 2

    answer.reverse()
    len_answer = len(answer)
    for j in range(len_answer):
        answer[j] = str(answer[j])

    print(len_answer)
    print(' '.join(answer))
