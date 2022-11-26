from collections import defaultdict


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    T = []
    for _ in range(H):
        S.append(input())

    for _ in range(H):
        T.append(input())

    S_rev = []

    for i in range(W):
        tmp = [None]*H
        for j in range(H):
            tmp[j] = S[j][i]
        tmp_txt = ''.join(tmp)
        S_rev.append(tmp_txt)

    T_rev = []

    for i in range(W):
        tmp = [None]*H
        for j in range(H):
            tmp[j] = T[j][i]
        tmp_txt = ''.join(tmp)
        T_rev.append(tmp_txt)

    d_t = defaultdict(int)
    d_s = defaultdict(int)

    for t in T_rev:
        d_t[t] += 1
    for s in S_rev:
        d_s[s] += 1

    for k in d_t:
        if d_t[k] == d_s[k]:
            pass
        else:
            print('No')
            break
    else:
        print('Yes')