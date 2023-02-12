from bisect import bisect
from collections import deque
import bisect
import itertools
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [0]
    B = [0]
    A2 = list(map(int, input().split()))
    for a in A2:
        A.append(a)
    B2 = list(map(int, input().split()))
    for b in B2:
        B.append(b)

    A_crr = list(itertools.accumulate(A))
    B_crr = list(itertools.accumulate(B))

    ans = 0
    for A_num in range(len(A_crr)):
        B_num = bisect.bisect_right(B_crr, K - A_crr[A_num]) -1
        if B_num < 0:
            continue
        ans = max(ans, A_num + B_num)

    print(ans)




