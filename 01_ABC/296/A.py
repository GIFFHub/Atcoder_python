

if __name__ == '__main__':
    N = int(input())
    S = input()
    tmp = ''
    for i in range(N):
        if S[i] != tmp:
            tmp = S[i]
        else:
            print('No')
            break

    else:
        print('Yes')
