

if __name__ == '__main__':
    X = input()
    i = X.index('.')
    ans = int(X[:i])
    if int(X[i+1]) <= 4:
        print(ans)
    else:
        print(ans+1)



