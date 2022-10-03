

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    m = 10**9+7

    for i in range(N):
        for j in range(i+1, N):
            ans += A[i] * A[j]

    print(ans % m)
