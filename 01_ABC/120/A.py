

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    money = B
    cnt = 0
    while True:
        money -= A
        if money < 0:
            break
        else:
            cnt += 1
        if cnt == C:
            break

    print(cnt)

