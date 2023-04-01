import bisect

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    for i in range(N):
        a = A[i]
        j = bisect.bisect_left(A, a+X)
        if 0 <= j < N:
            if A[j] == a+X:
                print('Yes')
                break
    else:
        print('No')
