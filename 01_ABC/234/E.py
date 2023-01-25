def check(N):
    str_N = str(N)
    len_N = len(str_N)
    tmp = int(str_N[1])- int(str_N[0])
    for i in range(2, len_N):
        if tmp == int(str_N[i])- int(str_N[i-1]):
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    X = input()
    len_X = len(X)
    int_X = int(X)
    if len_X == 1:
        ans = int_X
    elif len_X > 10:
        tmp = int(X[0] * len_X)
        if int_X > tmp:
            ans = int(str(int(X[0]) + 1) * len_X)
        else:
            ans = tmp
    elif len_X == 10:
        if 9876543210 >= int_X > 8888888888:
            ans = 9876543210
        else:
            tmp = int(X[0]*len_X)
            if int_X > tmp:
                ans = int(str(int(X[0])+1)*len_X)
            else:
                ans = tmp
    elif len_X == 9:
        if 987654321 >= int_X > 888888888:
            ans = 987654321
        elif 876543210 >= int_X > 777777777:
            ans = 876543210
        elif 123456789 >= int_X > 111111111:
            ans = 123456789
        else:
            tmp = int(X[0] * len_X)
            if int_X > tmp:
                ans = str(int(X[0]) + 1) * len_X
            else:
                ans = tmp
    elif len_X == 8:
        if 98765432 >= int_X > 88888888:
            ans = 98765432
        elif 87654321 >= int_X > 77777777:
            ans = 87654321
        elif 76543210 >= int_X > 66666666:
            ans = 76543210
        elif 23456789 >= int_X > 22222222:
            ans = 23456789
        elif 12345678 >= int_X > 11111111:
            ans = 12345678
        else:
            tmp = int(X[0] * len_X)
            if int_X > tmp:
                ans = str(int(X[0]) + 1) * len_X
            else:
                ans = tmp
    elif len_X == 7:
        if 9876543 >= int_X > 8888888:
            ans = 9876543
        elif 8765432 >= int_X > 7777777:
            ans = 8765432
        elif 7654321 >= int_X > 6666666:
            ans = 7654321
        elif 6543210 >= int_X > 5555555:
            ans = 6543210
        elif 3456789 >= int_X > 3333333:
            ans = 3456789
        elif 2345678 >= int_X > 2222222:
            ans = 2345678
        elif 1234567 >= int_X > 1111111:
            ans = 1234567
        else:
            tmp = int(X[0] * len_X)
            if int_X > tmp:
                ans = str(int(X[0]) + 1) * len_X
            else:
                ans = tmp
    else:
        while True:
            if check(int_X):
                ans = int_X
                break
            else:
                int_X += 1

    print(ans)

    '''
    ・10桁以上の等差数は全要素同じ値のみ
    ・以下全要素同じ値は可
        ・9桁
            123456789
            987654321
        ・8桁
            12345678
            23456789
            逆
        ・7桁
            1234567
            2345678
            3456789
            逆
        ・6桁
            123456
            234567
            345678
            456789
            逆
        ・5桁
            12345
            13579
            23456
            34567
            45678
            56789
        
    '''