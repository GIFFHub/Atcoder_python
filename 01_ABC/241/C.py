def check(table: list) -> bool:
    for i in range(len(table)):
        # 先頭に.があり条件を満たすパターン
        if table[i][0:6].count("#") >= 4:
            return True
        else:
            for j in range(1, max(1, len(table[0])-5)):
                if table[i][j] == '#':
                    if table[i][j+1:j+6].count("#") >= 3:
                        return True
    return False


def reverse_table(table: list) -> list:
    table_reverse = []
    for j in range(len(table[0])):
        tmp = ''
        for i in range(len(table)):
            tmp += table[i][j]
        table_reverse.append(tmp)
    return table_reverse


def slide_table_right(table: list) -> list:
    table_slide = []
    for i in range(len(table)):
        tmp = '$'*(N-i) + S[i] + '$'*i
        table_slide.append(tmp[5:-5])
    return table_slide


def slide_table_left(table: list) -> list:
    table_slide = []
    for i in range(len(table)):
        tmp = '$'*i + S[i] + '$'*(N-i)
        table_slide.append(tmp[5:-5])
    return table_slide


if __name__ == '__main__':
    # input
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    if N < 6:
        print('No')
    else:

        S_reverse = reverse_table(S)
        S_slide_right = reverse_table(slide_table_right(S))
        S_slide_left = reverse_table(slide_table_left(S))

        ans_horizontal = check(table=S)
        ans_vertical = check(table=S_reverse)
        ans_slide_right = check(table=S_slide_right)
        ans_slide_left = check(table=S_slide_left)

        if ans_vertical or ans_horizontal or ans_slide_right or ans_slide_left:
            print('Yes')
        else:
            print('No')






