import math
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

    l = prime_factorize(K)
    if l[-1] >= 10**(6):
        print(l[-1])
        exit()

    tmp = 1
    for i in range(2, K):
        if tmp >= K and tmp % K == 0:
            print(i-1)
            break
        tmp *= i

