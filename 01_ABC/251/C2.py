
if __name__ == '__main__':

    # 初期化
    S = []
    T = []
    best_score = -1
    best_index = -1

    # 入力
    N = int(input())
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    # 既出のポエムかどうかを記録
    appeared = set()

    # ポエム一つ一つを既出か、暫定１位かで判定していく。O(N)で済む。
    for i in range(N):
        # 既出のポエムの場合何もしない（最優秀になることはない）
        if S[i] in appeared:
            continue

        # 既出でない場合は記録
        appeared.add(S[i])

        # 暫定１位として更新
        if best_score < T[i]:
            best_score = T[i]
            best_index = i

    print(best_index+1)


