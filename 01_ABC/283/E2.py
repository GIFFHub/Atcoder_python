

if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    '''
    ・方針としては、孤立していたら下の行を反転するというやり方でやる
    ・下の行反転後、再度その行について判定し直してダメならおわり
    ・行列の値を実際に反転すると時間が間に合わないので、
    　・上の行は反転したのか
    　・自身の行は反転したのか
    　・下の行は反転したのか
    　を判定時のINPUTとする。
    '''

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    cnt = 0
    flg = 1
    for i in range(1, H+1):
        tmp_flg = 1
        for j in range(1, W+1):
            pos = (i, j)
            # 孤立している場合
            if check(pos, 1, flg):
                for k in range(1, W+1):
                    pos = (i, k)
                    if check(pos, 2, flg):
                        print(-1)
                        exit()
                cnt += 1
                tmp_flg = 2
        flg = tmp_flg



    print(cnt)







