

if __name__ == '__main__':

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = [sum([(x+1)*A[x] for x in range(M)])]
    A_crr = []
    tmp = 0
    for i in range(N):
        A_crr.append(tmp+A[i])
        tmp = A_crr[i]

    dif = 0
    for j in range(N-M):
        if j == 0:
            dif = -(A_crr[j+M-1] - M*A[j+M])
        else:
            dif = -(A_crr[j+M-1] - A_crr[j-1] - M*A[j+M])
        sum_A.append(sum_A[j]+dif)

    print(max(sum_A))


