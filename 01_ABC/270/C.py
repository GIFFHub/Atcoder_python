
def search(prev_start, start, goal):
    global ans

    for i in range(len(side)):
        if side[i][0] == start:
            if side[i][1] == goal:
                return True
            elif side[i][1] != prev_start:
                if search(start, side[i][1], goal):
                    ans.append(side[i][1])
                    return True

        elif side[i][1] == start:
            if side[i][0] == goal:
                return True
            elif side[i][0] != prev_start:
                if search(start, side[i][0], goal):
                    ans.append(side[i][0])
                    return True

    return False


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    side = []
    for _ in range(N-1):
        u, v = map(int, input().split())
        side.append([u, v])

    ans = [Y]
    search(-1, X, Y)
    ans.append(X)
    ans.reverse()

    for j in range(len(ans)):
        if j == 0:
            print('%d' % ans[j], end='')
        else:
            print(' %d' % ans[j], end='')






