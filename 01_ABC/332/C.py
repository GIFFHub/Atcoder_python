if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input()
    ans = N
    T = 0
    for t in range(N):
        logo = t
        muji = M
        for i in range(N):
            if S[i] == '0':
                logo = t
                muji = M
            elif S[i] == '1':
                if muji > 0:
                    muji -= 1
                elif logo > 0:
                    logo -= 1
                else:
                    break
            elif S[i] == '2':
                if logo > 0:
                    logo -= 1
                else:
                    break
        else:
            ans = min(ans, t)

    print(ans)




