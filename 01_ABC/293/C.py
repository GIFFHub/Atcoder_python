from itertools import product


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    '''
    ・下にH-1回、右にW-1回移動する
    ・全探索する上で変わるのは、どのタイミングで下もしくは右に移動するか
    ・0000011111の順列
    
    '''
    ans = 0
    k = 1
    for pro in product((0, 1), repeat=H+W-2):
        if sum(pro) == H-1:
            x = 0
            y = 0
            S = set()
            S.add(A[x][y])
            for p in pro:
                if p == 1:
                    x += 1
                else:
                    y += 1
                if A[x][y] in S:
                    break
                else:
                    S.add(A[x][y])
            else:
                ans += 1
    print(ans)




