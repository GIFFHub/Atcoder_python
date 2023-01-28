
if __name__ == '__main__':
    S = input()
    T = input()
    len_T = len(T)

    pre = [False] * (len_T+1)
    suf = [False] * (len_T+1)
    pre[0] = True
    suf[0] = True
    for i in range(len_T):
        if S[i] == T[i] or S[i] == '?' or T[i] == '?':
            pre[i+1] = True
        else:
            break

    for j in range(len_T):
        if S[-j-1] == T[-j-1] or S[-j-1] == '?' or T[-j-1] == '?':
            suf[j+1] = True
        else:
            break

    for x in range(len_T+1):
        if pre[x] and suf[len_T-x]:
            print('Yes')
        else:
            print('No')
