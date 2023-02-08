import math


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def gcd_t(list_g1):
    for a in reversed(range(1, min(list_g1)+1)):
        for b in list_g1:
            if b % a != 0:
                break
        else:
            return a


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    d = ['not coprime', 'setwise coprime', 'pairwise coprime']

    ans = 0
    s = set()
    T = []
    for i in range(N):
        T.append(make_divisors((A[i])))
        for j in range(1, len(T[i])):
            if T[i][j] in s:
                break
            else:
                s.add(T[i][j])
        else:
            continue
        break
    else:
        ans = 2

    if ans != 2:
        if gcd_t(A) == 1:
            ans = 1

    print(d[ans])