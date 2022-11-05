import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    min_A = my_gcd(*A)
    ans = 0
    for a in A:
        if a % min_A != 0:
            print(-1)
            exit()
        else:
            if a == min_A:
                continue

            tmp = a//min_A

            if tmp % 2 != 0 and tmp % 3 != 0:
                print(-1)
                exit()
            while tmp >= 2 and tmp % 2 == 0:
                ans += 1
                tmp //= 2
            while tmp >= 3 and tmp % 3 == 0:
                ans += 1
                tmp //= 3

            if tmp != 1:
                print(-1)
                exit()

    print(ans)

