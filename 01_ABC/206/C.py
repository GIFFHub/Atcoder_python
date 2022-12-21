from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(int)
    for a in A:
        d[a] += 1

    ans = 0
    for i in range(N):
        ans += N - (i+1) - (d[A[i]]-1)
        d[A[i]] -= 1

    print(ans)



