from collections import deque
S = input()

dq = deque()
for s in S:
    dq.append(s)

dq.pop()
dq.appendleft('0')

for d in dq:
    print(d, end='')