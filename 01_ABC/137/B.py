

if __name__ == '__main__':
    K, X = map(int, input().split())
    left = max(-1000000, X-K)
    right = min(1000000, X+K)
    ans = []
    for x in range(left+1, right):
        ans.append(x)

    print(*ans)