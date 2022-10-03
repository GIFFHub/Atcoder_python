import sys
sys.setrecursionlimit(3000)
def check(n):
    '''
    チームの総合力としてnがありえるのか判定する
    :param n: チームの総合力
    :return: bool
    '''
    s = set()
    for ability in Ability:
        tmp = 0
        for i in range(5):
            if ability[i] >= n:
                tmp += 1 << i
        s.add(tmp)

    for i in s:
        for j in s:
            for k in s:
                if i | j | k == 31:
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
    N = int(input())
    Ability = [list(map(int, input().split())) for _ in range(N)]
    ok_0 = 0
    ng_0 = 10**9 + 1
    print(binary_search(ok_0, ng_0))


