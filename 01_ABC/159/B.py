def check(moji):
    len_moji = len(moji)
    for i in range(len_moji//2):
        if moji[i] != moji[-i-1]:
            return False
    return True


if __name__ == '__main__':
    S = input()
    N = len(S)
    S1 = S[:(N-1)//2]
    S2 = S[(N+3)//2-1:]

    if check(S) and check(S1) and check(S2):
        print('Yes')
    else:
        print('No')
