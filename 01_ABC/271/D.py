

N, S = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i][j] : i番目のカードまで使って、総和jにできるか否か

dp = [[False]*(S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(1, N+1):
    for j in range(0, S+1):
        if j-A[i-1] >= 0:
            if dp[i-1][j-A[i-1]]:
                dp[i][j] = True

        if j-B[i-1] >= 0:
            if dp[i-1][j-B[i-1]]:
                dp[i][j] = True

if dp[N][S]:
    print('Yes')
    ans = []
    for i in range(1, N+1):
        if dp[N-i][S-A[N-i]]:
            ans.append('H')
            S -= A[N-i]
        else:
            ans.append('T')
            S -= B[N-i]

    print(''.join(reversed(ans)))

else:
    print('No')








