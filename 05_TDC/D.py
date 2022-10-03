
def countdiv(x):
    cnt = 0
    global d
    while d % x == 0:
        d /= x
        cnt += 1
    return cnt


if __name__ == '__main__':
    n, d = map(int, input().split())

    # まずDが2と3と5を何回かけたものなのか調べる
    cnt_2 = countdiv(2)
    cnt_3 = countdiv(3)
    cnt_5 = countdiv(5)

    if d > 2: # 2,3,5以外の素因数がある場合
        print(0)
    else:
        dp = [[[[0] for _ in range(cnt_5)] for _ in range(cnt_3)] for _ in range(cnt_2)]









