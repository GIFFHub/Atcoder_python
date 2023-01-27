

if __name__ == '__main__':
    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))
    P.sort(reverse=True)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # if -1 <= (P[i][1] - P[j][1] / P[i][0] - P[j][0]) <= 1:
            if P[j][0] - P[i][0] <= P[i][1] - P[j][1] <= P[i][0] - P[j][0]:
                ans += 1

    print(ans)
