

if __name__ == '__main__':
    N = int(input())
    B = list(map(int, input().split()))
    ans = 0
    A = [0] * N

    for i in range(N-1):
        A[i] = B[i]
        if i >= 1:
            if B[i-1] < A[i]:
                A[i] = B[i-1]
        ans += A[i]
    ans += B[-1]

    print(ans)



