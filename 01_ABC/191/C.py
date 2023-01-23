

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())

    '''
    自身は黒として
    ・右上が角：右上が白、右と上が同じ
    ・左上が角：左上が白、左と上が同じ
    ・右下が角：右下が白、右と下が同じ
    ・左下が角：左下が白、左と下が同じ
    
    '''
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                # 右上が角：右上が白、右と上が同じ
                if S[i-1][j+1] == "." and S[i][j+1] == S[i-1][j]:
                    ans += 1
                # 左上が角：左上が白、左と上が同じ
                if S[i-1][j-1] == '.' and S[i][j-1] == S[i-1][j]:
                    ans += 1
                # 右下が角：右下が白、右と下が同じ
                if S[i+1][j+1] == '.' and S[i][j+1] == S[i+1][j]:
                    ans += 1
                # 左下が角：左下が白、左と下が同じ
                if S[i+1][j-1] == '.' and S[i][j-1] == S[i+1][j]:
                    ans += 1

    print(ans)