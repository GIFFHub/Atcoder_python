if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[] for _ in range(H)]
    B = [[] for _ in range(H)]
    for i in range(H):
        for s in input():
            A[i].append(s)
    for j in range(H):
        for s in input():
            B[j].append(s)

    A_ch = [[False] * W for _ in range(H)]
    for dx in range(W):
        for dy in range(H):
            for y in range(H):
                for x in range(W):
                    A_ch[y][x] = A[(y+dy)%H][(x+dx)%W]
            for a, b in zip(A_ch, B):
                if a != b:
                    break
            else:
                print('Yes')
                exit()

    print('No')


