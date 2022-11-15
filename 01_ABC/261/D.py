N, M = map(int, input().split())
X = list(map(int, input().split()))
Bonus = dict()
for _ in range(M):
    c, y = map(int, input().split())
    Bonus[c] = y

'''

考察  
・ボーナスがあるカウンタとないカウンタがある  
・ボーナスがもらえるのは表が出たときだけ  
・序盤の連続ボーナスが莫大の場合やそもそもボーナス数が少ない場合、何度もそのボーナスをもらった方がいいため、  
　ずっと表の場合が最大になるとは限らない  
・コイントス前回の回数から今回の最大円計算できる？  
　→表が出たときの＋Xi分と、連続ボーナス＋Ci分
　→つまり、連続回数情報も前回からの遷移時に必要になる。

・横(j) 連続回数(0～N)× 縦(i) コイントス回数(0～N)の2次元DPで解ける？

dp[i][j] : コイントスi回目、連続回数j回目の時の最大ポイント


'''

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(N + 1):
        if j > i:
            continue

        if j == 0:
            dp[i][j] = max(dp[i - 1])

        else:
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
            if j in Bonus:
                dp[i][j] += Bonus[j]

# print(dp)
print(max(dp[N]))




