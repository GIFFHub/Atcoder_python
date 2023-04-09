

if __name__ == '__main__':
    S = input()
    X = len(S)
    B_flg = 0
    R_flg = 0
    N_flg = 0
    for i in range(X):
        if S[i] == 'B':
            if B_flg:
                B_index2 = i
            else:
                B_index = i
                B_flg = 1
        elif S[i] == 'K':
            K_index = i
        elif S[i] == 'R':
            if R_flg:
                R_index2 = i
            else:
                R_index = i
                R_flg = 1


    if B_index % 2 != B_index2 % 2:
        if R_index < K_index < R_index2:
            print('Yes')
            exit()

    print('No')
