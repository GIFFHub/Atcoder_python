

if __name__ == '__main__':
    X = input()

    if len(X) >= 3:
        if X[-1] == '0' and X[-2] == '0':
            print('Yes')
        else:
            print('No')
    else:
        print('No')