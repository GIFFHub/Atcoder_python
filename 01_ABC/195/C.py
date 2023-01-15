import math

if __name__ == '__main__':
    N = int(input())

    ans = 0
    T = [15, 12, 9, 6, 3]
    for t in T:
        c = 10**t
        if N >= c:
            ans += (N-c+1) * (t//3)
            N = c-1

    print(ans)
