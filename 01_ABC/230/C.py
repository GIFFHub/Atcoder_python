

if __name__ == '__main__':
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    query_1_start = max(1-A, 1-B)
    query_1_end = min(N-A, N-B)

    query_2_start = max(1-A, B-N)
    query_2_end = min(N-A, B-1)

    query_1_start = max(query_1_start, P-A)
    query_1_end = min(query_1_end, Q-B)

    query_2_start = max(query_2_start, R-A)
    query_2_end = min(query_2_end, S-B)

    paint_point = set()
    # query_1
    for k in range(query_1_start, query_1_end+1):
        tmp_x = A+k
        tmp_y = B+k

        if P <= tmp_x <= Q and R <= tmp_y <= S:
            paint_point.add((tmp_x, tmp_y))

    # query_2
    for k in range(query_2_start, query_2_end+1):
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


