from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    S = set()
    M = 10**6
    d = defaultdict(int)
    ans = 0
    for a in A:
        d[a] += 1

    if A[0] == 1:
        if d[1] == 1:
            ans = 1
        else:
            ans = 0
    else:
        for a in A:
            if a not in S:
                tmp = a
                cnt = 2
                while tmp <= M:
                    tmp = a*cnt
                    S.add(tmp)
                    cnt += 1
        for a in A:
            if d[a] == 1:
                if a not in S:
                    ans += 1

    print(ans)



