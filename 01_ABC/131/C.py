import math


def calc(x):
    xc = x // C
    xd = x // D
    xcd = x // CD

    return x - xc - xd + xcd


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    CD = C*D//math.gcd(C, D)
    # 区間[a,b]の個数 = 区間[1,b]の個数 - 区間[1,a]の個数
    # f(x) = 区間[1,x]のうち、CでもDでも割り切れないものの個数
    # ans = f(B) - f(A-1)
    ans = calc(B)-calc(A-1)
    print(ans)
