import sys
sys.setrecursionlimit(5000000)


def check(current, flg):
    global tmp_visit
    global visit
    tmp_visit.add(current)
    visit.add(current)
    '''
    :param current: 現在の点
    :param flg: 1の場合はループになっている
    :return:
    '''
    nxt = A[current - 1]
    # 現状ループ状態でない場合
    if flg == 0:
        if dist[nxt - 1] > dist[current - 1]+1:
            return
        # 次の点が行ったことある点の場合
        if nxt in tmp_visit:
            dist[nxt-1] = -1
            check(nxt, 1)
        else:
            # 次の点へ移動するための距離は、前の点プラス１
            dist[nxt-1] = dist[current-1] + 1
            check(nxt, 0)
    # ループの場合
    else:
        # 次がループ状態になっていない場合はループにする
        if dist[nxt-1] != -1:
            dist[nxt-1] = -1
            check(nxt, 1)
        else:
            return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    # dist[i] : 点iに移動するために引き伸ばせる最大距離
    # -1の場合はループとする
    dist = [0]*N

    # 自分に移動する点がない点を調べる（スタート地点になりえる点）
    s = set()
    for i, a in enumerate(A):
        s.add(a)

    visit = set()
    # 全ての点について
    for p in range(1, N+1):
        # pに移動する点がない場合＝スタート足りえる点
        if p not in s:
            tmp_visit = set()
            # 次の点以降を調べる
            check(p, 0)

    # 調査で到達しなかった点はすべてループ
    for p in range(1, N+1):
        if p not in visit:
            dist[p-1] = -1
    ans = 0
    for x in range(N):
        if dist[x] == -1:
            ans += 1
        elif dist[x] == N:
            ans += 1
    print(ans)




