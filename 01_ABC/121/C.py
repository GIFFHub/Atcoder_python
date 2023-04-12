

if __name__ == '__main__':
    N, M = map(int, input().split())
    T = []
    for _ in range(N):
        a, b = map(int, input().split())
        T.append((a, b))

    T.sort()

    cnt = 0
    ans = 0
    for i in range(N):
        if cnt+T[i][1] <= M:
            cnt += T[i][1]
            ans += T[i][0]*T[i][1]
        else:
            rest = M - cnt
            ans += T[i][0]*rest
            break

    print(ans)
