import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    score = 0
    left = 0
    for i in range(N):
        x = A[i]
        right = bisect.bisect_left(A, x+M)
        score = max(score, right - i)

    for j in range(N):
        A[j] *= -1

    A.sort()
    for i in range(N):
        x = A[i]
        right = bisect.bisect_left(A, x+M)
        score = max(score, right - i)

    print(score)











