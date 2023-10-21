from collections import deque

if __name__ == '__main__':
    '''
    方針：まじめにDFSでやる
    '''

    H, W = map(int, input().split())

    S = []
    for _ in range(H):
        S.append(input())

    # 到達有無
    T = [[False] * W for _ in range(H)]

    # 移動ベクトル
    move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    ans = 0
    dq = deque()

    for i in range(H):
        for j in range(W):
            # 既に到達済みの場合
            if T[i][j]:
                continue
            else:
                # 未到達かつセンサ位置の場合
                if S[i][j] == '#':
                    ans += 1
                    dq.append((i, j))

                    while len(dq) > 0:
                        current_pos = dq.popleft()
                        for m in move:
                            y = current_pos[0] + m[0]
                            x = current_pos[1] + m[1]
                            if 0 <= x < W and 0 <= y < H:
                                if S[y][x] == '#':
                                    if not T[y][x]:
                                        T[y][x] = True
                                        dq.append((y, x))
    print(ans)










