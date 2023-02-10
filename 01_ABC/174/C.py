

if __name__ == '__main__':
    N = int(input())
    C = input()
    T = []
    '''
    以下二択
    　pattern 1 : 左側に白（False）が存在する赤（True)を全て左に持っていく
    　pattern 2 : 右側に赤（True）が存在する白（False）を全て赤に変える
    '''
    for c in C:
        if c == 'R':
            T.append(True)
        else:
            T.append(False)

    # 左側に白が存在する赤の数を数える
    flg = 0
    pattern1 = 0
    for t in T:
        if not t:
            flg = 1
        if flg and t:
            pattern1 += 1
    for i in range(pattern1):
        if T[i]:
            pattern1 -= 1

    # 右側に赤が存在する白の数を数える
    flg = 0
    pattern2 = 0
    T.reverse()
    for t in T:
        if t:
            flg = 1
        if flg and not t:
            pattern2 += 1

    print(min(pattern1, pattern2))


