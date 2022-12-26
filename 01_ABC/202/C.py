from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    C.sort()
    d = defaultdict(int)

    for c in C:
        d[B[c-1]] += 1

    ans = 0
    for a in A:
        ans += d[a]
    print(ans)



