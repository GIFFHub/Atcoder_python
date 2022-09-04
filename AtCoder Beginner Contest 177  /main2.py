

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    m = 10**9+7


    # 累積和を求める
    sum_A = [0]*N
    A_rev = list(reversed(A))
    for i in range(N):
        if i == 0:
            sum_A[i] = A_rev[i]
        else:
            sum_A[i] = sum_A[i-1] + A_rev[i]
    sum_A_rev = list(reversed(sum_A))
    for i in range(N-1):
        ans += A[i] * sum_A_rev[i+1]

    print(ans % m)

