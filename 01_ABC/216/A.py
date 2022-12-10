

if __name__ == '__main__':
    S = input()
    index = S.find('.')

    X = S[:index]
    Y = int(S[index+1:])

    if 0 <= Y <= 2:
        print(X+'-')
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X+'+')

