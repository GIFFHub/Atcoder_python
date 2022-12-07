import bisect


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    # dpの設定
    # dp[i] : 最後の要素がiである最長部分列
    dp = [0] * N
    dp[0] = 1

    # Lの設定
    # L[k] : 長さがkの部分列の最後の値となりうる最小値
    # →これがわかると、未知の値について、どの部分列の後ろにつけられるかがわかる
    # また、L[k+1]は、その未知の値が最小値となる

    L = [5*(10**6)+1] * (N+1)
    L[0] = 0

    # Aの各要素について調べていく
    for i in range(N):
        # A[i]がLのどの最長部分列の後ろにつくか調べる
        k = bisect.bisect_left(L, A[i])

        # 値iが最後になる最長部分列はk(値i以下で最も大きい値が最後になる最長部分列の長さ）+1
        dp[i] = k

        # 長さがk+1になる最長部分列は更新される
        if k < N+1:
            L[k] = min(A[i], L[k])

    print(max(dp))
