

if __name__ == '__main__':
    S = input()
    T = input()

    len_S = len(S)
    len_T = len(T)
    d = []
    if len_S != len_T:
        print('No')
        exit()
    else:
        for i in range(len_S):
            if S[i] != T[i]:
                d.append(i)

    if len(d) == 0:
        print('Yes')
    elif len(d) != 2:
        print('No')
    else:
        if S[d[0]] == T[d[1]] and S[d[1]] == T[d[0]]:
            if d[0] == d[1]-1:
                print('Yes')
            else:
                print('No')
        else:
            print('No')



