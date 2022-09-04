def binary_search(ok, ng): # 求めたい値になるかどうかでもok,ngで攻める
    if ng - ok == 1: # ok,ngがくっついたとき、判定もして求めたい値かどうかも判定して返す
        if A_cum[ok] - A_cum[x] == size:
            return True
        else:
            return False
    cen = (ng + ok) // 2

    if A_cum[cen] - A_cum[x] == size:
        return True
    elif A_cum[cen] - A_cum[x] > size:
        return binary_search(ok, cen)
    else:
        return binary_search(cen, ng)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    size = sum(A)/10 # 全体の大きさの10分の1
    A += A


    # 累積和
    A_cum = []
    tmp = 0
    for i in range(N*2):
        tmp += A[i]
        A_cum.append(tmp)

    for x in range(N):
        if binary_search(x-1, x+N): # 二分探索の引数はあくまで外側（長さ1でも-1と2でcenは0になる）
            print('Yes')
            break
    else:
        print('No')
