
if __name__ == '__main__':

    # 初期化
    H, W = map(int, input().split())
    A = [[ ]for x in range(H)]
    for line in range(H):
        A[line] = list(map(int, input().split()))

    A_line_sum = []
    A_row_sum =[]
    # 行ごとの合計を作成
    for line in range(H):
        A_line_sum.append(sum(A[line]))

    # 列ごとの合計を作成
    for row in range(W):
        tmp = 0
        for line in range(H):
            tmp += A[line][row]
        A_row_sum.append(tmp)

    # 出力
    for line in range(H):
        for row in range(W):
            ans = A_line_sum[line] + A_row_sum[row] - A[line][row]

            if row == 0:
                print('%d' % ans, end='')
            else:
                print(' %d' % ans, end='')
        print()
