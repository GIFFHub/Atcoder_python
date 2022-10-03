# A17 - Dungeon 2

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # dp[i] : i番目の部屋に行く最小の時間

    dp = [None] * (N+1)
    dp[1] = 0
    dp[2] = A[0]

    for i in range(3, N+1):
        dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

    ans = []
    Place = N
    while True:
        ans.append(Place)
        if Place == 1:
            break
        if dp[Place-1] + A[Place-2] == dp[Place]:
            Place -= 1
        else:
            Place -= 2

    ans.reverse()
    len_ans = len(ans)
    for j in range(len_ans):
        ans[j] = str(ans[j])

    print(len_ans)
    print(" ".join(ans))



