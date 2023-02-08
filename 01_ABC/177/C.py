

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    K = 10**9+7
    sum_A = sum(A)
    T = [0]*N
    for i in range(N):
        T[i] = sum_A-A[i]

    ans = 0
    for j in range(N):
        ans += (A[j] * T[j])
    ans //= 2
    ans %= K
    print(ans)


