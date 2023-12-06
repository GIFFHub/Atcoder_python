import bisect

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Q = int(input())
    for _ in range(Q):
        ans = 0
        b = int(input())
        index = bisect.bisect(A, b)
        if index == N:
            ans += b - A[index-1]
        elif index == 0:
            ans += A[0] - b
        else:
            ans += min(b-A[index-1], A[index]-b)
        print(ans)


