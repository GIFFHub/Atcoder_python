if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(H):
        B.append(list(map(int, input().split())))

    cnt = 0
    for y in range(H-1):
        for x in range(W-1):
            d = B[y][x] - A[y][x]
            if d != 0:
                cnt += abs(d)
            A[y][x] += d
            A[y][x+1] += d
            A[y+1][x] += d
            A[y+1][x+1] += d
            if x+1 == W-1:
                if B[y][x+1] != A[y][x+1]:
                    print('No')
                    exit()
            if y+1 == H-1:
                if B[y+1][x] != A[y+1][x]:
                    print('No')
                    exit()
            if x+1 == W-1 and y+1 == H-1:
                if B[y+1][x+1] != A[y+1][x+1]:
                    print('No')
                    exit()
    print('Yes')
    print(cnt)


