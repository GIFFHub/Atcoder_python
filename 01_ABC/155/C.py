
from collections import defaultdict
if __name__ == '__main__':
    N = int(input())
    S = []
    d = defaultdict(int)
    for _ in range(N):
        s = input()
        S.append(s)
        d[s] += 1

    M = max(d.values())
    ans = []
    for key, value in d.items():
        if value == M:
            ans.append(key)

    ans.sort()

    for a in ans:
        print(a)




