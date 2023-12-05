if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())

    direct = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    for i in range(H):
        for j in range(W):
            if S[i][j] == 's':
                for d in direct:
                    x = j
                    y = i
                    target = 'nuke'
                    for k in range(4):
                        x += d[1]
                        y += d[0]
                        if 0 <= y < H and 0 <= x < W:
                            if S[y][x] != target[k]:
                                break
                        else:
                            break
                    else:
                        ans_y = i+1
                        ans_x = j+1
                        print(ans_y, ans_x)
                        for _ in range(4):
                            ans_y += d[0]
                            ans_x += d[1]
                            print(ans_y, ans_x)
                        exit()









