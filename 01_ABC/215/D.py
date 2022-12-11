import math
from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = deque()
    s = set()
    for k in range(2, M+1):
        for t in s:
            if k % t == 0:
                break
        else:
            for a in A:
                if math.gcd(a, k) == 1:
                    pass
                else:
                    break
            else:
                ans.append(k)
                s.add(k)


    ans.appendleft(1)
    print(len(ans))
    for x in ans:
        print(x)


