

if __name__ == '__main__':
    S = input()
    T = input()
    len_S = len(S)
    len_T = len(T)
    S_h = []
    T_h = []
    for i, s in enumerate(S):
        if s == '?':
            S_h.append(i)
    for i, t in enumerate(T):
        if t == '?':
            T_h.append(i)
    


    for x in range(len_T+1):
        S2 = S[:x] + S[len_S-(len_T-x):]

        for i in range(len_T):
            if S2[i] != T[i]:
                if S2[i] == '?' or T[i] == '?':
                    continue
                else:
                    print('No')
                    break
        else:
            print('Yes')


