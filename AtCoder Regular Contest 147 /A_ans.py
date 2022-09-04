from collections import deque

input()

# 後ろから出して頭に入れる
A = deque(sorted(map(int, input().split())))

cnt = 0

while len(A) > 1:
    cnt += 1
    # popが一番早い
    x = A.pop() % A[0]
    if x != 0:
        A.appendleft(x)
        # A[0]が常に最小（0でない)になる

print(cnt)
