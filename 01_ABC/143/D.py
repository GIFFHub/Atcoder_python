import bisect

if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            a = L[i]
            b = L[j]
            # a-b < c < a+b
            # L[j+1:]で上記を満たすcの数を二分探索で求める
            left = bisect.bisect_left(L[j+1:], b-a+1)
            right = bisect.bisect_right(L[j+1:], a+b-1)
            ans += right - left

    print(ans)
