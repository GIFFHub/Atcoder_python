
'''
・問題
　・Aを何度も連結して左から足す
　・合計がXを超えたところのインデックスを求める

・方針
　・Aの合計を計算する
　・X//Aの合計を計算する
　・そこからXを超えるまで１つずつ足していき調べる

'''

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    # Aの合計を計算
    A_sum = sum(A)

    # XはAの合計何個分（Aの要素何個分）より大きいか
    C = X // A_sum
    C_in = C * N
    # Xを超えるまで計算
    tmp = C * A_sum
    for i, a in enumerate(A):
        tmp += a
        if X < tmp:
            print(C_in + (i+1))
            break






