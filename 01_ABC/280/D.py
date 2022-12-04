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

    ans = []
    for x, y in d.items():
        cnt = 0
        t = x
        s = y
        while True:
            cnt += prime_factorize(t).count(x)
            if cnt >= y:
                ans.append(t)
                break
            else:
                t += x
    #print(d)
    #print(ans)
    print(max(ans))







