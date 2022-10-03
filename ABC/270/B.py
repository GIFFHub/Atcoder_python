
X, Y, Z = map(int, input().split())

if X > 0:
    if Y < 0:
        print(X)
    elif 0 < Y < X:
        if 0 < Z < Y:
            print(X)
        elif Z < 0:
            print(X + 2*abs(Z))
        else:
            print(-1)
    else:
        print(X)

else:
    if 0 < Y:
        print(abs(X))
    elif X < Y < 0:
        if Z < Y:
            print(-1)
        elif Y < Z < 0:
            print(abs(X))
        else:
            print(2*Z + abs(X))
    else:
        print(abs(X))

