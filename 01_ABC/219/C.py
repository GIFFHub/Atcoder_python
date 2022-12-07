import string

if __name__ == '__main__':
    X = input()
    N = int(input())
    S = []
    alp = list(string.ascii_uppercase)
    for _ in range(N):
        S.append(input())

    d = dict()
    for i, x in enumerate(X):
        d[x] = alp[i]

    S_change = []
    for j, s in enumerate(S):
        tmp = ''
        for s_1 in s:
            tmp += d[s_1]
        ap_list = [tmp, j]
        S_change.append(ap_list)

    S_change.sort()

    for sc in S_change:
        print(S[sc[1]])
