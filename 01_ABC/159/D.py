
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    ans = 0
    for x in d.values():
        if x > 1:
            ans += x*(x-1)//2

    for k in range(1, N+1):
        tmp_ans = ans
        if d[A[k-1]] > 1:
            tmp_ans -= d[A[k-1]]*(d[A[k-1]]-1)//2
            tmp_ans += (d[A[k-1]]-1)*(d[A[k-1]]-2)//2
        print(tmp_ans)


