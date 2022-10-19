def check(x, y, dx, dy):
    cnt = 0
    for _ in range(6):
        if x >= N or y < 0 or y >= N:
            return False
        if S[y][x] == '#':
            cnt += 1
        x += dx
        y += dy
    if cnt >= 4:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    Dx = [0, 1, 1, 1]
    Dy = [1, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            for di, dj in zip(Dx, Dy):
                if check(j, i, di, dj):
                    print('Yes')
                    exit()

print('No')

