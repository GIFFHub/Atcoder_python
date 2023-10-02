

if __name__ == '__main__':

    N, D = map(int, input().split())
    days = [0 for _ in range(D)]
    for _ in range(N):
        S = input()
        for i, s in enumerate(S):
            if s == 'o':
                days[i] += 1

    cnt = 0
    ans = 0
    for d in days:
        if d == N:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)



