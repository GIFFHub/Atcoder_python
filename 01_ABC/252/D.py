

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    d_min = dict()
    d_min[A[0]] = 0
    for i in range(1, N):
        if A[i-1] != A[i]:
            d_min[A[i]] = i

    A.sort(reverse=True)
    d_max = dict()
    d_max[A[0]] = 0
    for i in range(1, N):
        if A[i-1] != A[i]:
            d_max[A[i]] = i

    ans = 0
    for a in A:
        ans += d_min[a]*d_max[a]

    print(ans)



