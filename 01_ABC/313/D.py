

if __name__ == '__main__':
    N, K = map(int, input().split())

    Q = []
    X = list(range(1, K+1))
    Q.append(X)
    ans = []

    if K > 1:
        Y = list(range(2, K+1))
        for i in range(1, N-K+1):
            Y_tmp = Y.copy()
            Y_tmp.append(Y[-1] + i)
            Q.append(Y_tmp)

        T = list(range(1, N+1))
        for j in range(1, K):
            Q.append(T[:j]+T[j+1:K]+[T[-1]])

        for q in Q:
            print('?', *q)
            ans.append(input())

    else:
        for q in range(N):
            print('?', q+1)
            ans.append(input())

    A = [0]*N
    A[0] = 1

    for t in range(1, N-K+1):
        if ans[0] == ans[t]:
            A[K+t-1] = 1

    for n in range(1, K):
        if ans[0] == ans[N-K+n]:
            A[n] = A[-1]
        else:
            A[n] = 1-A[-1]

    if sum(A[:K]) % 2 != int(ans[0]):
        for i in range(N):
            A[i] = 1 - A[i]
    print('!', *A)








