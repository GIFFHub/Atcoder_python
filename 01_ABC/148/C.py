import math

if __name__ == '__main__':
    A, B = map(int, input().split())
    c = A*B//math.gcd(A, B)
    print(c)