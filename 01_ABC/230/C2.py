

if __name__ == '__main__':
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    paint_point = set()
    # query_1
    # P <= A+k <= Q
    # P-A <= k <= Q-A
    # R <= B+k <= S
    # R-B <= k <= S-B
    for k in range(P-A-1, Q-A+1, 1):
        tmp_x = A+k
        tmp_y = B+k

        if P <= tmp_x <= Q and R <= tmp_y <= S:
            paint_point.add((tmp_x, tmp_y))

    # query_2
    for k in range(R-B-1, S-B+1, 1):
        tmp_x = A+k
        tmp_y = B-k

        if P <= tmp_x <= Q and R <= tmp_y <= S:
            paint_point.add((tmp_x, tmp_y))

    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i, j) in paint_point:
                print('#', end='')
            else:
                print('.', end='')
        print()


