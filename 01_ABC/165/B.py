

if __name__ == '__main__':
    X = int(input())
    # 公比1.01の等比数列

    cnt = 0
    money = 100
    while True:
        tmp = money // 100
        money += tmp
        cnt += 1
        if money >= X:
            print(cnt)
            break