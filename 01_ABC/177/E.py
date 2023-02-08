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


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = ['not coprime', 'setwise coprime', 'pairwise coprime']

    ans = 2
    s = set()
    for i in range(N):
        T = make_divisors((A[i]))
        for j in range(1, len(T)):
            if T[j] in s:
                ans = 1
                break
            else:
                s.add(T[j])
        else:
            continue
        break

    if math.gcd(*A) != 1:
        ans = 0

    print(d[ans])