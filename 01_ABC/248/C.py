N, M, K = map(int, input().split())

# dp[i][j] : 数列項目i個目までで、合計がjになるような場合の数

dp = [[0]*(K+1) for _ in range(N+1)]
T = 998244353 

for j in range(1, M+1):
  dp[1][j] = 1 # 数列

for i in range(1, N):
  for j in range(1, K+1):
    for k in range(1, M+1):
      if j+k <= K:
        dp[i+1][j+k] += dp[i][j]

#print(dp)
ans = sum(dp[N][:])
print(ans % T)



