import sys


if __name__ == '__main__':

    N, M = map(int, input().split())

    # d[i][j]: 都市iから都市jへの移動時間を全て無限大で初期化する
    d = [[1 << 60] * N for i in range(N)]

    # 同一都市の移動時間は0にする
    for i in range(N):
        d[i][i] = 0

    # inputを元に、都市iから都市jへの移動時間を設定する
    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a - 1][b - 1] = c

    ans = 0
    for k in range(N):
        # nxt[i][j]: 都市iから都市jへの移動時間？
        nxt = [[0] * N for i in range(N)]

        for i in range(N):
            for j in range(N):
                nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if nxt[i][j] < 1 << 59:
                    ans += nxt[i][j]
        # 各kでdを更新していくことで、各kを経由してたどり着ける都市までの移動時間を
        # 更新していく→それを次のnxtの計算に利用する
        d = nxt
    print(ans)
