

if __name__ == '__main__':
    N, K = map(int, input().split())
    ans = 0
    MOD = 10**9 + 7
    A = list(range(0, N+1))
    # 小さい方からK個と、大きい方からK個で全通りがある
    # F
    # 選ぶ個数によって合計値は異なる
    # 選ぶ個数をMとして固定して考える

    # 前からi番目までの合計の前計算
    front_S = [0]*(N+1)
    tmp = 0
    for i, a in enumerate(A):
        tmp += a
        front_S[i] = tmp
    # 後ろからi番目までの合計の前計算
    back_S = [0]*(N+1)
    tmp = 0
    for j, b in enumerate(reversed(A)):
        tmp += b
        back_S[j] = tmp

    for M in range(K, N+2):
        # M個選ぶ時の最小値
        min_sum = front_S[M-1]
        max_sum = back_S[M-1]
        ans += max_sum - min_sum + 1
        ans %= MOD

    print(ans)






