

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())

    for i in range(H):
        flg = 1
        ans = ''
        for j in range(W-1):
            if flg:
                if S[i][j] == 'T':
                    if S[i][j+1] == 'T':
                        ans+='PC'
                        flg = 0
                        continue
                ans+=S[i][j]
            else:
                flg = 1
        if flg:
            ans+=S[i][j+1]
        print(ans)




