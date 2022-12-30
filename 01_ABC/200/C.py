from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    D = defaultdict(int)
    for a in A:
        D[a % 200] += 1

    ans = 0
    for d in D.values():
        if d > 1:
            ans += d * (d-1) // 2

    print(ans)


