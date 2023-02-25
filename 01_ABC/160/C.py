

if __name__ == '__main__':
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    M = A[0] + (K-A[-1])
    for i in range(1, N):
        M = max(M, A[i]-A[i-1])

    print(K-M)


