import math


# エラトステネスの篩
# n以下の素数リストを返す
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False

    # 素数判定を基に, 素数リストを作成
    prime_list = []
    for i in range(n + 1):
        if is_prime[i]:
            prime_list.append(i)
    return prime_list


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


# O(√N)
def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    N = int(input())
    if N == 1:
        print(0)
        exit()
    P_list = prime(10**6+1)
    if P_list[-1] < N:
        P_list.append(N)
    div_N = make_divisors(N)

    s = set()
    for p in P_list:
        tmp = 1
        while tmp <= N:
            tmp *= p
            s.add(tmp)
    for d in div_N:
        if is_prime(d):
            s.add(d)
    cnt = 0
    for d in div_N[1:]:
        if N % d == 0:
            if d in s:
                N //= d
                cnt += 1

    print(cnt)






