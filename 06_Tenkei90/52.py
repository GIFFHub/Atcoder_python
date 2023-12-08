if __name__ == '__main__':
    N = int(input())
    K = 10**9 + 7
    ans = 1
    for _ in range(N):
        A = list(map(int, input().split()))
        sum_A = sum(A)
        ans *= sum_A
        ans %= K

    print(ans)