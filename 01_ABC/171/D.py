from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    d = dict()
    ans = sum(A)
    A_cnt = defaultdict(int)
    for a in A:
        A_cnt[a] += 1

    for i in range(Q):
        b, c = map(int, input().split())
        ans += (c-b)*A_cnt[b]
        A_cnt[c] += A_cnt[b]
        A_cnt[b] = 0

        print(ans)




