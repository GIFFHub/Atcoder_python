from collections import defaultdict

if __name__ == '__main__':
    N, C = map(int, input().split())
    d = defaultdict(int)
    for i in range(N):
        a, b, c = map(int, input().split())
        d[a] += c
        d[b+1] -= c
    days = list(d.keys())
    days.sort()
    moneys = [d[days[0]]]
    for j in range(1, len(days)):
        tmp = moneys[j-1] + d[days[j]]
        moneys.append(tmp)

    ans = 0
    for k in range(len(moneys)-1):
        # お金が発生する期間
        term = days[k+1] - days[k]
        # その間発生するお金
        money = moneys[k]

        pay = min(money, C)

        ans += pay*term

    print(ans)
