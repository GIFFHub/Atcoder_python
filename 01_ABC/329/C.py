

if __name__ == '__main__':
    N = int(input())
    S = input()
    d = dict()

    tmp = 1 # 何連続続いたか
    for i in range(N):
        if not i == 0:
            if S[i-1] == S[i]:
                tmp += 1
            else:
                tmp = 1
        if S[i] in d:
            d[S[i]] = max(d[S[i]], tmp)
        else:
            d[S[i]] = tmp

    ans = 0
    for value in d.values():
        ans += value

    print(ans)



