

if __name__ == '__main__':
    S = input()
    ans = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] not in {'R', 'U', 'D'}:
                break
        else:
            if S[i] not in {'L', 'U', 'D'}:
                break
    else:
        ans = 1

    if ans == 1:
        print('Yes')
    else:
        print('No')
