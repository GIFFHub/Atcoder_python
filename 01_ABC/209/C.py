

if __name__ == '__main__':
    N = int(input())
    C = list(map(int, input().split()))
    T = 10**9+7
    C.sort()
    ans = C[0]
    for i in range(1, N):
        ans *= C[i]-i
        ans %= T

    print(ans)
