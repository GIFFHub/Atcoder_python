X, K = map(int, input().split())

for i in range(K):
    X_str = str(X)
    tmp = X_str[-(i+1):]
    if int(tmp) >= 5*10**i:
        X -= int(tmp)
        X += 10**(i+1)
    else:
        X -= int(tmp)

print(X)





