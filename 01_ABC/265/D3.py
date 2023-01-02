import bisect

if __name__ == '__main__':
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    A_crr = [0]
    tmp = 0
    for a in A:
        tmp += a
        A_crr.append(tmp)

    '''
    A[x]-A[i] = PなるA[x]のインデックスを求める
    A[x] = P + A[i]になる
    A[x]をA_crrについて二分探索する
    '''
    for i in range(N-2):
        target = P + A_crr[i]
        y = bisect.bisect_right(A_crr, target)
        if target == A_crr[y-1]:
            target = Q + A_crr[y-1]
            z = bisect.bisect_right(A_crr, target)
            if target == A_crr[z-1]:
                target = R + A_crr[z-1]
                w = bisect.bisect_right(A_crr, target)
                if target == A_crr[w-1]:
                    print('Yes')
                    exit()

    print('No')
