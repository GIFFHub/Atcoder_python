

if __name__ == '__main__':
    S = list(map(int, input().split()))

    tmp = -1
    for s in S:
        if s < 100 or s > 675:
            print('No')
            break
        if s % 25 != 0:
            print('No')
            break
        if s < tmp:
            print('No')
            break
        tmp = s

    else:
        print('Yes')