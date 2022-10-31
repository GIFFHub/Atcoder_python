
def power(x, k, m):
    p = x
    ans = 1
    for i in range(30):
        w = 2**i
        # kを2進数表記した際の、右からi桁目が1である場合
        if (k//w) % 2 == 1:
            #ans = (ans*p) % m
            ans *= p
            ans %= m

        p = (p*p) % m
    return ans


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(power(a, b, 100))

