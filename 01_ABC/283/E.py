def check(p, mode, f):
    if mode == 1:
        for i in range(4):
            dpx = p[0] + dx[i]
            dpy = p[1] + dy[i]

            if 1 <= dpx <= H and 1 <= dpy <= W:
                if f == 1:
                    if A[p[0]-1][p[1]-1] == A[dpx-1][dpy-1]:
                        return False
                else:
                    if A[p[0]-1][p[1]-1] != A[dpx-1][dpy-1]:
                        return False
        return True

    elif mode == 2:
        for i in range(4):
            dpx = p[0] + dx[i]
            dpy = p[1] + dy[i]

            if 1 <= dpx <= W and 1 <= dpy <= H:
                if i == 0:
                    if f == 1:
                        if A[p[0]-1][p[1]-1] != A[dpx-1][dpy-1]:
                            return False
                    else:
                        if A[p[0]-1][p[1]-1] == A[dpx-1][dpy-1]:
                            return False

                else:
                    if f == 1:
                        if A[p[0]-1][p[1]-1] == A[dpx-1][dpy-1]:
                            return False
                    else:
                        if A[p[0]-1][p[1]-1] != A[dpx-1][dpy-1]:
                            return False
        return True


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    cnt = 0
    flg = 1
    for i in range(1, H+1):
        tmp_flg = 1
        for j in range(1, W+1):
            pos = (i, j)
            # 孤立している場合
            if check(pos, 1, flg):
                for k in range(1, W+1):
                    pos = (i, k)
                    if check(pos, 2, flg):
                        print(-1)
                        exit()
                cnt += 1
                tmp_flg = 2
        flg = tmp_flg



    print(cnt)







