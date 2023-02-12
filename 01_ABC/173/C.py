from itertools import product

if __name__ == '__main__':
    H, W, K = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())

    ans = 0
    for h in product((0, 1), repeat=H):
        for w in product((0, 1), repeat=W):
            tmp = 0
            for i in range(H):
                for j in range(W):
                    if h[i] and w[j] and C[i][j] == '#':
                        tmp += 1

            if tmp == K:
                ans += 1

    print(ans)
