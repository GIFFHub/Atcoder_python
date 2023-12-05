if __name__ == '__main__':
    N = int(input())
    S = input()

    T_num = 0
    A_num = 0
    for s in S:
        if s == 'T':
            T_num += 1
        else:
            A_num += 1

    if T_num > A_num:
        print('T')
    elif T_num < A_num:
        print('A')
    else:
        if S[-1] == 'A':
            print('T')
        else:
            print('A')


