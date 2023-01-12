

if __name__ == '__main__':
    H, W, X, Y = map(int, input().split())
    S = ['#'*(W+2)]
    for _ in range(H):
        S.append('#'+input()+'#')
    S.append('#'*(W+2))

    if S[X][Y] == '#':
        ans = 0
    else:
        ans = 1

        # 上チェック
        cnt = 1
        while True:
            if S[X][Y+cnt] == '.':
                ans += 1
                cnt += 1
            else:
                break

        # 下チェック
        cnt = 1
        while True:
            if S[X][Y-cnt] == '.':
                ans += 1
                cnt += 1
            else:
                break

        # 右チェック
        cnt = 1
        while True:
            if S[X+cnt][Y] == '.':
                ans += 1
                cnt += 1
            else:
                break

        # 左チェック
        cnt = 1
        while True:
            if S[X-cnt][Y] == '.':
                ans += 1
                cnt += 1
            else:
                break

        print(ans)



