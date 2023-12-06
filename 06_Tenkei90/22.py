import math

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    lcm = math.gcd(A, B, C)

    print(A//lcm+B//lcm+C//lcm-3)