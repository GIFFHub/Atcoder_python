
if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [[] for _ in range(K)]
    A_sorted = []
    if K == 1:
        print('Yes')
    else:
        for i in range(N):
            B[i % K].append(A[i])

        for j in range(K):
            B[j] = sorted(B[j])

        # print(B)
        for i in range(N):
            j = i % K
            A_sorted.append(B[j][(i-j)//K])
        # print(A_sorted)
        A.sort()
        if A == A_sorted:
            print('Yes')
        else:
            print('No')



