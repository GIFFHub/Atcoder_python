

if __name__ == '__main__':
    N = int(input())
    CRR = []
    tmp = 1
    money = 0
    cnt = 0
    while True:
        cnt += 1
        money += tmp
        tmp += 1
        if money >= N:
            print(cnt)
            break

