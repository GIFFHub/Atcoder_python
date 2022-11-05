from collections import defaultdict

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A_sum = []
    tmp = 0
    for i in range(N):
        tmp += A[i]
        A_sum.append(tmp)

    ans = 0

    d = defaultdict(int)
    d[0] = 1
    for r in range(N):
        ans += d[A_sum[r]-K]
        d[A_sum[r]] += 1

    print(ans)




