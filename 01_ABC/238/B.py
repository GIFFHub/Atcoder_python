
if __name__ == '__main__':
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # 初期角度から、何度の位置に切れ込みが入っているか記録する
    # 時計回りに回して12時の方向に切る　＝　反時計回り◯◯°の方向に切る

    tmp = 0
    cut = [0]
    for a in A:
        tmp += a
        tmp %= 360
        cut.append(tmp)
    cut.append(360)

    # 最も大きい切り込み間角度値が答え
    # ソートして、切り込み間角度を最大値で更新すれば良い

    cut.sort()
    ans = 0
    tmp = 0
    for c in cut:
        ans = max(ans, c-tmp)
        tmp = c

    print(ans)
