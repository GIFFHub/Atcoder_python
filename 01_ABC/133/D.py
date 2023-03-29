

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    flg = 1
    for i in range(N):
        ans[0] += flg*A[i]
        flg *= (-1)
    for j in range(1, N):
        ans[j] = 2*A[j-1] - ans[j-1]
    print(*ans)


