
def base10int(value, base):
    if (int(value // base)):
        return base10int(int(value // base), base) + str(value % base)
    return str(value % base)


if __name__ == '__main__':
    N, K = map(int, input().split())
    tmp_8 = str(N)
    for _ in range(K):
        tmp_10 = int(tmp_8, 8)
        tmp_9 = base10int(tmp_10, 9)
        s = ''
        flg = 0
        for t in tmp_9:
            if t == '8':
                s += '5'
            else:
                s += t
            flg = 1
        tmp_8 = s

    print(tmp_8)