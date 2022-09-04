import math
import seaborn as sns

def cal_gcd(a, b):

    if a > b:
        c = a % b
        if c != 0:
            return cal_gcd(b, c)
        else:
            return b

    else:
        c = b % a
        if c != 0:
            return cal_gcd(a, c)
        else:
            return a

if __name__ == '__main__':

    cake = list(map(int, input().split()))

    # ケーキの各辺を大きい順にソートする
    cake.sort(reverse=True)

    # 最大公約数が、切り分けた後の立方体の辺の長さになる

    # 最大公約数
    # l = math.gcd(cake[0], cake[1], cake[2])
    l = cal_gcd(cake[0], cake[1])
    l = cal_gcd(l, cake[2])

    ans = 0
    for i in range(len(cake)):
        if l != 0:
            ans += cake[i] // l - 1

    print(ans)
