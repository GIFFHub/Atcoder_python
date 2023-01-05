from collections import defaultdict


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
    d = defaultdict(int)
    B = []
    for a in A:
        d[a] += 1

    ans = 0
    for i in range(N):
        divs = make_divisors(A[i])
        for div in divs:
            if div in d:
                if A[i] // div in d:
                    ans += d[div] * d[A[i]//div]

    print(ans)

