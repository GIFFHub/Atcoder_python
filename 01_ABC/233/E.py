

if __name__ == '__main__':
    X = input()
    X_int = int(X)

    keta = len(X)
    ans = X_int
    for i in range(keta-1):
        tmp = int(X[:-i-1])
        if tmp == 0:
            break
        else:
            ans += tmp

    print(ans)






