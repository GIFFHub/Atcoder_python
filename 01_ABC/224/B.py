

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [[] for _ in range(H)]

    for i in range(H):
        grid[i] = list(map(int, input().split()))

    for i1 in range(H-1):
        for i2 in range(i1+1, H):
            for j1 in range(W-1):
                for j2 in range(j1+1, W):
                    if grid[i1][j1]+grid[i2][j2] > grid[i2][j1]+grid[i1][j2]:
                        print('No')
                        exit()

    print('Yes')
