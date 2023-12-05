if __name__ == '__main__':
    N = int(input())
    S = input()
    T = input()

    flg = 0
    for s, t in zip(S, T):
        if s == t:
            pass
        elif s == '1' and t == 'l':
            pass
        elif s == '0' and t == 'o':
            pass
        elif t == '1' and s == 'l':
            pass
        elif t == '0' and s == 'o':
            pass
        else:
            flg = 1
            break

    if flg:
        print('No')
    else:
        print('Yes')


