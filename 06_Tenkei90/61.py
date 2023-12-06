from collections import deque

if __name__ == '__main__':
    Q = int(input())
    dq = deque()
    ans = []
    for _ in range(Q):
        t, x = map(int, input().split())

        if t == 1:
            dq.appendleft(x)
        elif t == 2:
            dq.append(x)
        else:
            ans.append(dq[x-1])

    for a in ans:
        print(a)

