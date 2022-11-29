
'''
考察
・開始が早い順にソートする
・上から順見ていって、最初に終了が来る壁を見つける
・その壁の右列でパンチ→これまで見てきた壁と、最初に終了がきた壁と、
　その後ろの開始がパンチラインに重なっている壁を破壊
・以降次に最初に終了が来る壁を見つける
・問題は、どうやって、最初に終了が来る壁を見つけるか
・

'''


if __name__ == '__main__':
    N, D = map(int, input().split())
    wall = []
    for _ in range(N):
        l, r = map(int, input().split())
        wall.append([l, r])

    wall.sort(key=lambda x: x[1])

    ans = 0 # パンチ回数
    line = 0 # どこまで壊したか
    for i in range(N):
        if line < wall[i][0]:
            line = wall[i][1]+D-1
            ans += 1

    print(ans)


