N = int(input())
S = input()
T = input()

'''
考察
・ハミング距離は、異なるbitの個数
・異なるbitの個数が、S, Tと同じUの最小を求める
・SとTで同じbitの部分からは、Uのハミング距離も同じ
・SとTで異なるbitの部分から、同じbit, 異なるbitの数を同じにすればよい
・つまり存在しない＝（-1）となるのは、異なるbitの部分の数が奇数の時
・辞書順に並べるためには、共通部分は全部0, 左側をできるだけ0,右側をできるだけ1になるように並べればよい
'''

# まずSとTでどこが同じでどこが異なるか調べる
flg = [False] * N
for i in range(N):
    if S[i] == T[i]:
        flg[i] = True

cnt_False = flg.count(False)
if cnt_False % 2 > 0:
    print(-1)
else:
    ans = [0] * N
    cnt_S = cnt_False // 2
    cnt_T = cnt_False // 2

    for j in range(N):
        if not flg[j]:
            if S[j] == '1':
                if cnt_S > 0:
                    cnt_S -= 1
                else:
                    ans[j] = 1
            elif T[j] == '1':
                if cnt_T > 0:
                    cnt_T -= 1
                else:
                    ans[j] = 1

    for a in ans:
        print(a, end='')
