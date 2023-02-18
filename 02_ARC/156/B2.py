

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = set(A)
    mod = 998244353
    T = N + K + 1
    # M[i]:iを初めて黒板に書くために必要な操作回数 (0<=i<=Max_A)
    M = [0]*T
    cnt = 1
    for i in range(T):
        M[i] = cnt
        if i not in S:
            cnt += 1

    # 階乗前計算
    fact = [0]*T
    tmp = 1
    for i in range(1, T+1):
        tmp *= i
        tmp %= mod
        fact[i-1] = tmp

    ans = 0
    for x in range(T):
        # M回はxを初めて書くために使うので、残りの操作回数はK-M
        # K-M回の操作で0~xを追加する重複組み合わせ
        # (K-M+x)! // (K-M)! // x!
        ans += fact[K-M-x] // (fact[K-M] * fact[x])

    ans %= mod
    print(mod)










