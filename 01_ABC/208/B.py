

if __name__ == '__main__':
    P = int(input())
    coins = []

    tmp = 1
    for i in range(1, 11):
        tmp *= i
        coins.append(tmp)

    ans = 0
    cnt = 1
    while cnt < 11:
        if P >= coins[-cnt]:
            ans += P // coins[-cnt]
            P = P % coins[-cnt]
        cnt += 1

    print(ans)
