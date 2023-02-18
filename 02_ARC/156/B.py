

def binom(n, r):
    return fac[n] * finv[n-r] % MOD * finv[r] % MOD


if __name__ == '__main__':

    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 前処理
    MOD = 998244353
    table_len = 5 * (10**5)
    exi = [0] * 400001

    # 階乗
    fac = [1, 1]
    inv = [1, 1]
    finv = [1, 1]
    for i in range(2, table_len):
        fac.append(fac[-1] * i % MOD)
        inv.append(-inv[MOD % i] * (MOD // i) % MOD)
        finv.append(finv[-1] * inv[-1] % MOD)

    for v in A:
        exi[v] = 1
    need, res = 1, 0
    for i in range(N + K):
        if need > K:
            break
        rest = K - need
        res += binom(rest + i, i)
        res %= MOD
        if not exi[i]:
            need += 1

    print(res)



