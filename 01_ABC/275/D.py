def func(x):
    global d

    if x == 0:
        return 1
    else:
        if x in key:
            return d[x]
        if x//2 in key:
            tmp_2 = d[x//2]
        else:
            tmp_2 = func(x//2)
            key.add(x//2)
            d[x//2] = tmp_2
        if x//3 in key:
            tmp_3 = d[x//3]
        else:
            tmp_3 = func(x//3)
            key.add(x//3)
            d[x//3] = tmp_3
        return tmp_2 + tmp_3


if __name__ == '__main__':
    N = int(input())
    d = dict()
    key = set()
    print(func(N))