

if __name__ == '__main__':
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            tmp = str(i)+'0'+str(j)
            ans += int(tmp)

    print(ans)
