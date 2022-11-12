
if __name__ == '__main__':

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    tmp = 0
    T = []
    for i in range(N):
        if i == 0:
            tmp = A[i]
        else:
            if A[i] == A[i-1] or A[i] == A[i-1]+1:
                tmp += A[i]

            else:
                T.append(tmp)
                tmp = A[i]
    T.append(tmp)

    if M == A[-1]+1 and A[0] == 0:
        T[-1] += T[0]

    print(max(0, sum(A) - max(T), 0))
