from collections import deque
from collections import defaultdict
if __name__ == '__main__':
    N, A, B = map(int, input().split())
    S = input()
    dq = deque(list(S))
    T = []
    d = defaultdict(int)
    for i in range(N):
        for j in range(N//2):
            if dq[j] != dq[N-j-1]:
                d[i] += 1
        tmp = dq.popleft()
        dq.append(tmp)
        T.append(dq.copy())

    # i : A円払う回数
    # d[i] : B円払う回数

    ans = 10**9 * 5000 + 1
    for i in range(N):
        if i in d:
            ans = min(ans, A*i + B*d[i])
        else:
            ans = min(ans, A*i)

    print(ans)





