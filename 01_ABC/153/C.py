

if __name__ == '__main__':
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort(reverse=True)

    if len(H) <= K:
        ans = 0
    else:
        ans = sum(H[K:])

    print(ans)