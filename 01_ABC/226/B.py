

if __name__ == '__main__':
    N = int(input())
    table = [[] for _ in range(N)]
    for i in range(N):
        table[i] = list(map(int, input().split()))

    '''
    考察
    ・条件はLが等しいことと、同じ列のaが等しいこと
    ・つまり、1列目とk列目が等しいものということ
    ・等しいかどうかの判定は配列ごと
    ・全要素数が2×10**5
    ・まずLでソートして、要素が全一致しているかどうか見る
    '''

    table.sort()
    cnt = 0
    for j in range(N-1):
        # Lが同じかどうか判定
        if table[j][0] == table[j+1][0]:
            for k in range(1, table[j][0]+1):
                if table[j][k] == table[j+1][k]:
                    pass
                else:
                    break
            else:
                cnt += 1
    print(N-cnt)




