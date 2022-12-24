

if __name__ == '__main__':
    S = input()

    if S == '0':
        print(0)
        exit()

    tmp = S.count('00')
    ans = len(S) - tmp
    print(ans)


