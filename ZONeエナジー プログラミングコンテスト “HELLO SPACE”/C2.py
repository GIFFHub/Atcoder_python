N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]

def check(x): # 二分探索の真ん中を入れる（x が答え足りえるのかを検証する）
    """

    :param x: 答え候補。ありえるかどうか返すからCHECK。ありえるありえないで二分探索する
    :return: bool ありえるかありえないか
    """
    s = set()
    for a in A:
        # 集合sに加えていく。
        # 1 を0~5でbitシフトした値のうち、x（判定基準）より大きいものの合計
        tmp = 0
        for i in range(5):
            if a[i] >= x: # 各能力値の方が、判定対象値以上→判定値を実現できる場合
                tmp += 1 << i
                # 1をiだけシフトずらしたものを加算していく
                # →i番目が1のtmpができる！
                # →加算していくことで、各能力が判定値以上の場合1の5bit値ができる

        s.add(tmp) # sは５つの5bit値の集合になる
        # s.add(sum(1 << i for i in range(5) if a[i] >= x))

        for x in s:
            for y in s:
                for z in s:
                    # x, y, z の論理和が31の場合
                    # チームの総合力としてありえる
                    # チーム全体の能力が全て、基準値を満たす
                    # 5bitの or（論理和）が全て1になる
                    if x | y | z == 31:
                        return True
        return False

ok = 0 # チームの総合力としてありえる最小値
ng = 10**9 + 1 # チームの総合力としてありえる最大値

# ngが大きい側

while ng - ok > 1: # 前の答えととなりあわせになったら
    cen = (ok + ng) // 2 # cen はcenter
    if check(cen): # 答えがありえるなら、最大値求めるためにもっと大きい値も試しに行く
        ok = cen
    else: # 答えとしてありえないなら、もう少しちいさくしないといけない
        ng = cen
print(ok)

