

if __name__ == '__main__':
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        p1, p2, p3 = map(int, input().split())
        P.append(p1+p2+p3)

    '''
    考察
    ・明確なボーダーラインが決まるはず
    ・他の人が全員0点かつ、自分が満点の場合が、最高に順位が上がる条件
    　→つまり、自分の点数を+300して、点数がK番以内ならOK
    ・現状の順位を出す
    ・現状K番目の人の点数を出す
    ・K番目の人の点数から-300した点数がボーダーライン
    
    '''

    P_sort = sorted(P, reverse=True)
    border = P_sort[K-1]-300

    for p in P:
        if p < border:
            print('No')
        else:
            print('Yes')

