

if __name__ == '__main__':
    N = int(input())
    z_max = -10**9 - 1
    w_max = -10**9 - 1
    z_min = 10**9 + 1
    w_min = 10**9 + 1
    for _ in range(N):
        x, y = map(int, input().split())
        z_max = max(z_max, x+y)
        z_min = min(z_min, x+y)
        w_max = max(w_max, x-y)
        w_min = min(w_min, x-y)

    ans = max(z_max-z_min, w_max-w_min)

    print(ans)






