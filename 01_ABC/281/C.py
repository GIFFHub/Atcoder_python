import bisect

if __name__ == '__main__':
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    T %= sum_A

    A_crr = []
    tmp = 0
    for i in range(N):
        tmp += A[i]
        A_crr.append(tmp)

    #print(A_crr)
    #print(T)

    #print(bisect.bisect_left(A_crr, T))
    index = bisect.bisect_left(A_crr, T)
    if index == 0:

        print(index+1, T)
    else:
        print(index+1, T-A_crr[index-1])



