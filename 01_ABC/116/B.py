

if __name__ == '__main__':
    s = int(input())

    S = set()
    S.add(s)
    tmp = s
    cnt = 1
    while True:
        cnt += 1
        if tmp % 2 == 0:
            nxt = tmp // 2
        else:
            nxt = 3 * tmp + 1

        if nxt in S:
            print(cnt)
            break
        tmp = nxt
        S.add(tmp)



