import math

if __name__ == '__main__':
    N = int(input())
    A = sorted(list(map(int, input().split())))

    g = 0
    for i in range(N-1):
        g = math.gcd(g, abs(A[i]-A[i+1]))

    if g == 1:
        print(2)
    else:
        print(1)

