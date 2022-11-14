# input
from collections import deque

N = int(input())
T = deque()
X = deque()
A = deque()

for _ in range(N):
    t, x, a = map(int, input().split())
    T.append(t)
    X.append(x)
    A.append(a)

dp = [[0] * 5 for _ in range(t + 1)]

for i in range(1, t + 1):
    for j in range(5):
        if j > i:
            if len(T) > 0:
                if i == T[0]:
                    tmp_pos = X[0]
                    if tmp_pos == j:
                        T.popleft()
                        X.popleft()
                        A.popleft()
            continue

        if j > 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j])

        if j < 4:
            dp[i][j] = max(dp[i - 1][j + 1], dp[i][j])

        dp[i][j] = max(dp[i - 1][j], dp[i][j])

        if len(T) > 0:
            if i == T[0]:
                tmp_pos = X[0]
                if tmp_pos == j:
                    T.popleft()
                    X.popleft()
                    tmp_size = A.popleft()
                    dp[i][j] += tmp_size

print(max(dp[t]))

