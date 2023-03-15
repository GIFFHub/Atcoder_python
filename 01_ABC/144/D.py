
import math


if __name__ == '__main__':
    a, b, x = map(int, input().split())
    S = a*a*b
    if x >= S/2:
        h1 = x / (a**2)
        tan1 = (b-h1) / (a/2)
        ans1 = math.degrees(math.atan(tan1))
        print(ans1)
    else:
        h2 = 2*x / (a*b)
        tan2 = b / h2
        ans2 = math.degrees(math.atan(tan2))
        print(ans2)
