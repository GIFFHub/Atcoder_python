import copy

if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(N):
        B.append(list(map(int, input().split())))

    tmp_A = copy.deepcopy(A)
    A_ch = [[False]*N for _ in range(N)]
    for _ in range(6):
        for y in range(N):
            for x in range(N):
                A_ch[y][x] = tmp_A[N-x-1][y]
        tmp_A = copy.deepcopy(A_ch)
        for i in range(N):
            for j in range(N):
                if A_ch[i][j] == 1:
                    if B[i][j] == 0:
                        break
            else:
                continue
            break
        else:
            print('Yes')
            exit()
    print('No')
