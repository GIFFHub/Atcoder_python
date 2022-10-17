
def binary_search(ng, ok, table, target):
    '''

    :param ng: ぎりぎり壁がないところの行番号（または列番号）のindex
    :param ok: 壁がある行番号（または列番号）のindex
    :param table: 壁のindexのリスト
    :param target: 現在地
    :return: 壁がある行番号（または列番号）
    '''
    if ok - ng == 1:
        return table[ok]
    cen = (ng+ok)//2
    if table[cen] <= target:
        return binary_search(cen, ok, table, target)
    elif table[cen] > target:
        return binary_search(ng, cen, table, target)


if __name__ == '__main__':

    # input(マス、現在地)
    H, W, rs, cs = map(int, input().split())
    N = int(input())

    # 壁の場所を行、列ごとにdictで管理
    dict_r = {} # 各行にある壁の列番号 （行がKey）
    dict_c = {} # 各列にある壁の行番号　(列がKey)
    for _ in range(N):
        r, c = map(int, input().split())
        if r in dict_r:
            dict_r[r].append(c)
        elif c in dict_c:
            dict_c[c].append(r)
        else:
            dict_r[r] = [c]
            dict_c[c] = [r]

    # dict_r, dict_c のvalueの各listをソート
    for r_list, c_list in zip(dict_r.values(), dict_c.values()):
        r_list.sort()
        c_list.sort()

    # input(移動方向)
    Q = int(input())
    D = []
    L = []
    for _ in range(Q):
        d, l = input().split()
        D.append(d)
        L.append(int(l))

    # 移動
    for i in range(Q):
        if D[i] == 'L':
            if cs == 1:
                break

            distance = 10**9
            # rs行に壁がある場合
            if rs in dict_r.keys():
                # distance: 壁までの距離
                distance = binary_search(-1, len(dict_r[rs]), dict_r[rs], cs)-cs

            # move: 移動距離: 壁までの距離と、果てまでの距離と、移動予定距離　の最小値
            move = min(distance, cs, L[i])
            cs -= move

        if D[i] == 'R':
            if cs == W:
                break
            move = min(L[i], binary_search(-1, len(dict_r[rs]), dict_r[rs], cs) - cs)
            cs -= move
            cs += 1
        if D[i] == 'U':
            if rs == 0:
                break
            elif (rs-1, cs) in wall:
                break
            else:
                rs -= 1
        if D[i] == 'D':
            if rs == H:
                break
            elif (rs+1, cs) in wall:
                break
            else:
                rs += 1

        print(rs, cs)
