import string

if __name__ == '__main__':
    S = input()
    alf = list(string.ascii_uppercase)
    s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    s0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if len(S) != 8:
        print('No')
        exit()
    if S[0] in alf:
        if S[1] in s:
            if S[2] in s0:
                if S[3] in s0:
                    if S[4] in s0:
                        if S[5] in s0:
                            if S[6] in s0:
                                if S[7] in alf:
                                    print('Yes')
                                    exit()

    print('No')




