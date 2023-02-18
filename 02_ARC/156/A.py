

if __name__ == '__main__':
    T = int(input())

    '''
    ・表の個数が奇数だったらアウト
    ・偶数だったらN=3で2つとなりあってる時以外OK？
    
    '''
    for _ in range(T):
        N = int(input())
        S = input()
        if N == 3:
            if S == '110' or S == '011':
                print(-1)
                continue
        if N == 4:
            if S == '0110':
                print(3)
                continue
        one_num = S.count('1')
        if one_num % 2 == 1:
            print(-1)
        else:
            if one_num == 2:
                if '11' in S:
                    print(2)
                else:
                    print(one_num//2)
            else:
                print(one_num//2)





