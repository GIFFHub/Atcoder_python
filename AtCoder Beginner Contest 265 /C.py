

if __name__ == '__main__':
    H, W = map(int, input().split())
    G = []
    G.append('*'*(W+2))
    for i in range(H):
        G.append('*'+input()+'*')
    G.append('*'*(H+2))


    pos_x = 1
    pos_y = 1
    pos_history = set()
    while True:
        pos_history.add((pos_x, pos_y))
        if G[pos_x][pos_y] == 'U':
            pos_x -= 1

            if G[pos_x][pos_y] == '*':
                pos_x += 1
                print('%d %d' % (pos_x, pos_y))
                break

        elif G[pos_x][pos_y] == 'D':
            pos_x += 1
            if G[pos_x][pos_y] == '*':
                pos_x -= 1
                print('%d %d' % (pos_x, pos_y))
                break
        elif G[pos_x][pos_y] == 'L':
            pos_y -= 1
            if G[pos_x][pos_y] == '*':
                pos_y += 1
                print('%d %d' % (pos_x, pos_y))
                break
        elif G[pos_x][pos_y] == 'R':
            pos_y += 1
            if G[pos_x][pos_y] == '*':
                pos_y -= 1
                print('%d %d' % (pos_x, pos_y))
                break
        if (pos_x, pos_y) in pos_history:
            print(-1)
            break






