

if __name__ == '__main__':
    N, K = map(int, input().split())
    ans = 0
    while N >= K:
        N //= K
        ans += 1

    print(ans+1)
