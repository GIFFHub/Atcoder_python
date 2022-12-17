
if __name__ == '__main__':
    N, M = map(int, input().split())
    S = []
    for _ in range(N):
        tmp = ''
        for s in input():
            if s == 'o':
                tmp += '1'
            else:
                tmp += '0'
        #S.append(tmp)
        S.append(int(tmp, 2))

    all = int('1'*M, 2)

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] | S[j] == all:
                ans += 1

    print(ans)


