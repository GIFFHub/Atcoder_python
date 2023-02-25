

if __name__ == '__main__':
    N, K = map(int, input().split())
    S = list(input())

    # Xの個数
    xc = 0
    for s in S:
        if s == 'X':
            xc += 1

    # Xの数より、操作できる回数の方が多い場合
    # →Xを全てYにしても操作が残っており、YをXにする必要がある場合
    if xc < K:
        # 全て変換した状態から考えて、どこを変換しないことにするか、という問題に帰着できる
        for i, s in enumerate(S):
            if s == 'Y':
                S[i] = 'X'
            elif s == 'X':
                S[i] = 'Y'
        # K箇所変換する＝N-K箇所変換しない
        # つまり全変換した状態からN-K箇所元に戻す
        K = N - K

    # Yの位置配列
    l = []
    for i, s in enumerate(S):
        if s == 'Y':
            l.append(i)

    # YとYの間にいくつXがあるか
    sumika = []
    for i in range(len(l) - 1):
        sumika.append(l[i+1] - l[i] - 1)

    # Yの位置の間隔を小さい順にソート
    # Xの連続が短いところから変えていくため
    sumika.sort()

    ans = 0
    for i in sumika:
        # Xの連続(sumika[i])よりも残り操作回数の方が多い場合
        if K >= i:
            K -= i
            ans += i+1

    # Yが存在する場合
    if len(l) > 0:
        # 両サイドの残りXをK回分Yにする
        ans += K
    else:
        # Yが存在しない場合
        # 確定でK-1になる（マイナスにはならない）
        # sumikaやxcの計算もない
        ans += max(0, K-1)

    print(ans)