

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [-1]*(M+1)

    B[M] = C[N+M] // A[N]

    for i in range(1, M+1):
        '''
        # i = 1
        C[N+M-1] = (A[N]*B[M-1] + A[N-1]*B[M])
        B[M-1] = (C[N+M-1] - A[N-1]*B[M]) // A[N]

        # i = 2 (N=1, M=2)
        C[N+M-2] = (A[N]*B[M-2] + A[N-1]*B[M-1] + A[N-2]*B[M])
        14 = 1*B[M-2] + 2*4 + 1*2
        
        B[M-2] = (C[N+M-2] - A[N-1]*B[M-1] - A[N-2]*B[M]) // A[N]
        '''

        tmp = 0
        for j in range(i):
            if N-1-j >= 0 and M+1+j-i >= 0:
                tmp += A[N-1-j]*B[M+1+j-i]

        B[M-i] = (C[N+M-i] - tmp) // A[N]

    print(*B)

