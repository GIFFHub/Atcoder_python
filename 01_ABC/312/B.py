

if __name__ == '__main__':
    N, M = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())

    for y in range(N):
        for x in range(M):
            if x <= M-9 and y <= N-9:
                if S[y][x:x+4] == '###.':
                    if S[y+1][x:x+4] == '###.':
                        if S[y+2][x:x+4] == '###.':
                            if S[y+3][x:x+4] == '....':
                                if S[y+5][x+5:x+9] == '....':
                                    if S[y+6][x+5:x+9] == '.###':
                                        if S[y+7][x+5:x+9] == '.###':
                                            if S[y+8][x+5:x+9] == '.###':
                                                print(y+1, x+1)


