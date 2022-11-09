

if __name__ == '__main__':
    S = input()
    K = int(input())

    len_S = len(S)
    T = []
    # example ...XXX..XX.X. K=2
    cnt = 0
    for i in range(len_S):
        if S[i] == 'X':
            cnt += 1
        else:
            T.append(cnt)
            cnt = 0
        if i == len_S-1:
            T.append(cnt)

    len_T = len(T)
    ans = 0
    #print(T)
    cnt_point = S.count('.')
    if K >= cnt_point:
        ans = len_S
    else:
        ans = sum(T[:K+1])+K
        tmp = ans
        for j in range(len_T-K-1):
            tmp = tmp - T[j] + T[K+j+1]
            ans = max(ans, tmp)

    print(ans)



