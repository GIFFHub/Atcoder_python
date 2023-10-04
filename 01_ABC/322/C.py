import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(1, N+1):
        day = bisect.bisect_left(A, i)

        print(A[day]-i)

