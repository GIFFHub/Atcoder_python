

if __name__ == '__main__':
    X = input()
    X1 = X[0]
    X2 = X[1]
    X3 = X[2]
    X4 = X[3]

    ans = 'Strong'
    if X1 == X2 == X3 == X4:
        ans = 'Weak'
    elif int(X2) == (int(X1) + 1) % 10:
        if int(X3) == (int(X2) + 1) % 10:
            if int(X4) == (int(X3) + 1) % 10:
                    ans = 'Weak'

    print(ans)
