

if __name__ == '__main__':

    # input()
    S = input()
    T = input()

    # prepare the alphabet dictionary
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_dict = dict()
    cnt = 0
    for a in alp:
        alp_dict[a] = cnt
        cnt += 1

    # judge the size
    len_S = len(S)
    len_T = len(T)
    if len_S != len_T:
        print('No')
        exit()

    # check the index differences of S
    diff_S = []
    for i in range(1, len_S):
        diff_S.append((alp_dict[S[i]] - alp_dict[S[i-1]])%26)

    # check whether Takahashi make S equal T
    for j in range(1, len_T):
        if (alp_dict[T[j]] - alp_dict[T[j-1]])%26 == diff_S[j-1]:
            pass
        else:
            print('No')
            break
    else:
        print('Yes')







