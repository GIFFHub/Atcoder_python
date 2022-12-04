from collections import defaultdict

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


if __name__ == '__main__':
    K = int(input())
    d = defaultdict(int)
    prime = prime_factorize(K)

    for a in prime:
        d[a] += 1

    print(prime)
    print(d)
    ans = []
    for x, y in d.items():
        t = x
        s = y
        cnt = 1
        while True:
            if t % s**y == 0:
                ans.append(cnt)
                break
            else:
                t *= x
                cnt += 1



        ans.append(x*y)







