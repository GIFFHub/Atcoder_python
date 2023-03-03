from functools import reduce


def cmb(n, r, p):
    r = min(n - r, r)
    if r == 0:
        return 1
    numer = reduce(lambda x, y: (x*y)%p, range(n, n - r, -1))
    denom = reduce(lambda x, y: (x*y)%p, range(1, r + 1))
    return (numer * pow(denom, p-2, p)) % p


p = 10 ** 9 + 7
