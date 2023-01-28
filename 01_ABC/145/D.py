from math import factorial

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


if __name__ == '__main__':
    X, Y = map(int, input().split())
    ans = 0
    if (X+Y) % 3 == 0:
        # (X, Y)にはn回移動してたどり着く
        n = (X+Y) // 3
        # x方向にa回、y方向にb回移動したとする
        a = X-n
        b = n-a
        ans = factorial

        p = 10 ** 9 + 7
        N = 10 ** 6  # N は必要分だけ用意する
        fact = [1, 1]  # fact[n] = (n! mod p)
        factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
        inv = [0, 1]  # factinv 計算用

        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % p)
            inv.append((-inv[p % i] * (p // i)) % p)
            factinv.append((factinv[-1] * inv[-1]) % p)

        ans = cmb(a+b, b, p)

    print(ans)






