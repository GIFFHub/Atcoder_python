import math

if __name__ == '__main__':
    R, X, Y = map(int, input().split())

    distance = math.sqrt(X**2 + Y**2)

    if distance < R:
        ans = 2

    elif distance % R == 0:
        ans = distance // R
    else:
        ans = distance // R + 1

    print(int(ans))

