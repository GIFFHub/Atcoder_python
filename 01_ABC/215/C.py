
import itertools
from collections import deque

if __name__ == '__main__':
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    arr = list(itertools.permutations(S))
    ans = deque()
    s = set()
    for x in arr:
        if x not in s:
            ans.append(x)
            s.add(x)

    print(''.join(ans[K-1]))