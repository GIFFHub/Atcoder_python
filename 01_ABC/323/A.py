

if __name__ == '__main__':
    S = input()
    for i in range(2, 17, 2):
        if S[i-1] == '0':
            pass
        else:
            print('No')
            break
    else:
        print('Yes')
