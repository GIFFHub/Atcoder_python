

if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input()

    # 文字列Sの各文字の色
    C = list(map(int, input().split()))

    # 各色の位置リスト
    Color_pos = [[] for _ in range(M)]
    for i, c in enumerate(C):
        Color_pos[c-1].append(i)


    d = dict()
    for one_color_pos in Color_pos:
        len_one_color_pos = len(one_color_pos)
        for i in range(len_one_color_pos):
            if i != len_one_color_pos-1:
                d[one_color_pos[i+1]] = one_color_pos[i]
            else:
                d[one_color_pos[0]] = one_color_pos[i]

    for i in range(N):
        print(S[d[i]], end='')




