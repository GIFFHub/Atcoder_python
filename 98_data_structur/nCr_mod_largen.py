from functools import reduce


def cmb(n, r, p):
    # nCr と n-rCrは同じなので小さい方にする
    r = min(n - r, r)
    # rが0なら必ず1
    if r == 0:
        return 1

    # 分子
    numer = reduce(lambda x, y: (x*y)%p, range(n, n - r, -1))
    # 分母
    denom = reduce(lambda x, y: (x*y)%p, range(1, r + 1))

    return (numer * pow(denom, p-2, p)) % p


p = 10 ** 9 + 7
