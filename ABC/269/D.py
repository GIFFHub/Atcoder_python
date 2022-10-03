
def gethex(x):

    round_hex = [
                    # (x[0], x[1]),
                    (x[0]-1, x[1]-1),
                    (x[0]-1, x[1]),
                    (x[0], x[1]-1),
                    (x[0], x[1]+1),
                    (x[0]+1, x[1]),
                    (x[0]+1, x[1]+1)
                ]

    for tmp_hex in round_hex:
        if tmp_hex in Hex:
            Hex.remove(tmp_hex)
            gethex(tmp_hex)


if __name__ == '__main__':
    N = int(input())
    Hex = set()
    ans = 0
    for _ in range(N):
        tmp_x, tmp_y = map(int, input().split())
        Hex.add((tmp_x, tmp_y))

    while len(Hex) > 0:
        tmp = Hex.pop()
        gethex(tmp)
        ans += 1

    print(ans)







