from collections import defaultdict

if __name__ == '__main__':
    N, K = map(int, input().split())

    d = defaultdict(int)
    S = 0
    target_days = set()
    for _ in range(N):
        a, b = map(int, input().split())
        S += b
        d[a+1] += b
        target_days.add(a+1)

    target_days = list(target_days)
    target_days.sort()

    ans = 1
    if S <= K:
        pass
    else:
        for td in target_days:
            S -= d[td]
            if S <= K:
                ans = td
                break

    print(ans)















