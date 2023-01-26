

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = A[0]
    for l in range(N):
        tmp_min = A[l]
        for r in range(l, N):
            tmp_min = min(tmp_min, A[r])
            ans = max(ans, tmp_min*(r-l+1))

    print(ans)



