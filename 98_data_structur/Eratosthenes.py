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
        if prime[i]:
            prime_list.append(i)
    return prime_list




