

if __name__ == '__main__':
    T = []
    for i in range(5):
        T.append(int(input()))

    m = 10
    ind = -1
    for i in range(5):
        if T[i] % 10 != 0 and m > T[i] % 10:
            ind = i
            m = T[i] % 10
    last = T.pop(ind)
    ans = 0
    for i in range(4):
        if T[i] % 10 == 0:
            ans += T[i]
        else:
            ans += 10*(T[i]//10 + 1)
    ans += last
    print(ans)