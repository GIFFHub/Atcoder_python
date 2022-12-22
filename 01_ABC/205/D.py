import bisect

if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    B_crr = []
    tmp = 0
    for i in range(N):
        B.append(A[i]-tmp-1)

        tmp = A[i]
        if i == 0:
            B_crr.append(B[i])
        else:
            B_crr.append(B_crr[i-1] + B[i])
    #print('A:', A)
    #print('B:', B_crr)
    K = []
    for _ in range(Q):
        K = int(input())
        K_index = bisect.bisect_left(B_crr, K)
        if K_index == 0:
            print(K)
        else:
            print(A[K_index-1]+K-B_crr[K_index-1])



