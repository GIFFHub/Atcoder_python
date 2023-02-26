import math

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    T = X[N:-N]
    sum_T = sum(T)
    ans = sum_T / (3*N)

    print(ans)