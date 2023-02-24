import math

def gcd_t(list_g1):
    for a in reversed(range(1, min(list_g1)+1)):
        for b in list_g1:
            if b % a != 0:
                break
        else:
            return a


if __name__ == '__main__':
    K = int(input())

    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            gcd_ab = math.gcd(a, b)
            if gcd_ab == 1:
                ans += K
            else:
                for c in range(1, K+1):
                    gcd_abc = math.gcd(gcd_ab, c)
                    ans += gcd_abc

    print(ans)
