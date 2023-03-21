

if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    cnt = 0
    ans = 0
    for i in range(1, N):
        if H[i] <= H[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)
