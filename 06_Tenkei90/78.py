from collections import defaultdict

if __name__ == '__main__':
    N, M = map(int, input().split())
    d = defaultdict(int)
    T = [True] * N
    for _ in range(M):
        a, b = map(int, input().split())
        if a < b:
            d[b] += 1
        else:
            d[a] += 1

    ans = 0
    for value in d.values():
        if value == 1:
            ans += 1

    print(ans)






