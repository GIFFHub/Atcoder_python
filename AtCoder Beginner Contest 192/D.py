
def get_max_num(d):
    for i in range(9, 0, -1):
        if str(i) in d:
            return i
    return


def base_10(num_n: str, n: int):
    """
    :param num_n: 10進数の文字列
    :param n: 進数
    :return: 10進数をn進数にした値
    """

    num_10 = 0
    for s in num_n:
        num_10 *= n
        num_10 += int(s)
    return num_10


def check(t):
    if base_10(x, t) <= m:
        return True
    return False


def binary_search(ok, ng):
    if ng - ok == 1:
        return ok

    cen = (ng + ok) // 2
    if check(cen):
        return binary_search(cen, ng)
    else:
        return binary_search(ok, cen)


if __name__ == '__main__':
    x = input()
    m = int(input())
    d = get_max_num(x)

    ok_0 = d
    ng_0 = 10**18+1

    if len(x) == 1:
        if int(x[0]) <= m:
            print(1)
        else:
            print(0)
    else:
        print(binary_search(ok_0, ng_0) - d)

    # print(binary_search(ok_0, ng_0) - d)
