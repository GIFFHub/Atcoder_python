

if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()
    tmp = S[0]
    T = []
    cnt = 0
    for s in S:
        if s != tmp:
            T.append(cnt)
            cnt = 0
        cnt += 1
        tmp = s
    T.append(cnt)

    T_crr = [0]
    tmp = 0
    for t in T:
        tmp += t
        T_crr.append(tmp)
    print(T)
    print(T_crr)

    L = len(T_crr)
    if K > L:
        ans = sum(T)
    else:
        for j in range(K, L):
            ans = T_crr[j] - T_crr[j-K]





