

def check(T):
    for n in range(1, 10):
        if n in T:
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    A = []
    for i in range(9):
        A.append(list(map(int, input().split())))

    flg = 0 # 0: 条件を満たす。 1:条件を満たさない。

    # 条件１チェック
    for j in range(9):
        check_list = A[j]
        if check(check_list):
            pass
        else:
            flg = 1

    # 条件２チェック
    if flg == 0:
        for k in range(9):
            if flg == 1:
                break

            check_list = []

            for l in range(9):
                check_list.append(A[l][k])
            if check(check_list):
                pass
            else:
                flg = 1

    # 条件３チェック
    if flg == 0:
        X = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        check_list = []
        for x1 in X:
            for x2 in X:
                for x1s in x1:
                    for x2s in x2:
                        check_list.append(A[x1s][x2s])
                if check(check_list):
                    pass
                else:
                    flg = 1
                check_list = []

    if flg:
        print('No')
    else:
        print('Yes')


