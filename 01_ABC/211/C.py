

if __name__ == '__main__':
    S = input()
    target = 'chokudai'
    len_S = len(S)
    len_t = len(target)

    ans = [[0] * len_S for _ in range(len_t)]

    for i, t in enumerate(target):
        for j, s in enumerate(S):
            if t == s:
                ans[i][j] = 1

    tmp = 0
    for j, s in enumerate(S):
        tmp += ans[0][j]
        ans[0][j] = tmp

    for i in range(1, len_t):
        for j in range(i, len_S):
            if j == i:
                ans[i][j] = ans[i][j] * ans[i-1][j-1]
            else:
                ans[i][j] = ans[i][j] * ans[i-1][j-1] + ans[i][j-1]

    print(ans[-1][-1]%(10**9+7))












