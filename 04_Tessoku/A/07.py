

D = [0] * (int(input())+1)
for _ in range(int(input())):
    L, R = map(int, input().split())
    D[L-1] += 1
    D[R] -= 1

D.pop()
ans = 0
for d in D:
    ans += d
    print(ans)


'''
・なぜ+1するのか
　D日目までいる場合、D[D] -= 1 することになるため
　配列の長さはD+1にしておく必要があるから

・実装方針
　参加者が増える日を+1、減る日を-1する配列を作る
　後で累積和を求めれば、各日の参加者数がわかる
'''





