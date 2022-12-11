from collections import deque


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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    s = set()
    for x in A:
        fact = prime_factorize(x)
        fact = set(fact)
        for f in fact:
            s.add(f)

    ans = deque()
    ans.append(1)
    for i in range(2, M+1):
        for y in s:
            if i % y == 0:
                break
        else:
            ans.append(i)

    print(len(ans))
    for an in ans:
        print(an)


