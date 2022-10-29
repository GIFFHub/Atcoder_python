
if __name__ == '__main__':
    S = []
    for _ in range(9):
        S.append(input())

    ans = 0
    for dx in range(-9, 10):
        for dy in range(-9, 10):
            if dx == dy == 0:
                continue
            for x in range(0, 9):
                for y in range(0, 9):
                    if S[x][y] == '#':
                        if 0 <= x+dx < 9 and 0 <= y+dy < 9:
                            if S[x+dx][y+dy] == '#':
                                if 0 <= x-dy < 9 and 0 <= y+dx < 9:
                                    if S[x-dy][y+dx] == '#':
                                        if 0 <= x+dx-dy < 9 and 0 <= y+dx+dy < 9:
                                            if S[x+dx-dy][y+dx+dy] == '#':
                                                ans += 1

    print(ans//4)


