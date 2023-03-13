

if __name__ == '__main__':
    N = int(input())
    S = input()

    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alf2 = alf+alf
    d = dict()
    for i in range(len(alf)):
        d[alf[i]] = alf2[i+N]
    ans = ''
    for s in S:
        ans += d[s]

    print(ans)


