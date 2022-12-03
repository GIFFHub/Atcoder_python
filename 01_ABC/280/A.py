

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    ans = 0
    for _ in range(H):
        s = input()
        ans += s.count('#')

    print(ans)