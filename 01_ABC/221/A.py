import math

if __name__ == '__main__':
    A, B = map(int, input().split())

    d = abs(A-B)
    ans = math.pow(32, d)

    print(int(ans))
