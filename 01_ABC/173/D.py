

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = A[0]
    tmp = 1
    flg = 0
    for i in range(2, N):
        ans += A[tmp]
        if flg:
            tmp += 1
        flg = 1-flg
    print(ans)



