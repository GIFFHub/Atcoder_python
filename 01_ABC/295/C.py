from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    d = defaultdict(inft)
    A = list(map(int, input().split()))

    for a in A:
        d[a] += 1

    ans = 0
    for values in d.values():
        ans += values//2

    print(ans)



