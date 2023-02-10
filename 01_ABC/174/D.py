

if __name__ == '__main__':
    N = int(input())
    C = input()
    T = []
    '''
    以下二択
    　pattern 1 : 左側に白（False）が存在する赤（True)を全て左に持っていく
    　pattern 2 : 右側に赤（True）が存在する白（False）を全て赤に変える
    '''
    if len(C) == 1:
        ans = 0
    elif len(C) == 2:
        if C == 'WR':
            ans = 1
        else:
            ans = 0
    else:
        for c in C:
            if c == 'R':
                T.append(True)
            else:
                T.append(False)

        Fs = []
        tmp = 0
        for t in T:
            if not t:
                tmp += 1
            else:
                Fs.append(tmp)

        Ts = []
        T.reverse()
        tmp = 0
        for t in T:
            if t:
                tmp += 1
            else:
                Ts.append(tmp)

        ans = min(Ts[-2], Fs[-2])
    print(ans)


