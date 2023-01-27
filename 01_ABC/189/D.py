import sys
sys.setrecursionlimit(50000000)


def count(cnt, tobe, ptn):
    global ans
    if cnt == N:
        ans += ptn
        return
    # 次をTrueにしたい
    if tobe:
        if S[cnt] == 'AND':
            # True-True
            count(cnt+1, True, ptn)
        else:
            # True-True
            # True-False
            # False-True
            count(cnt+1, True, ptn*2)
            count(cnt+1, False, ptn)

    # 次をFalseにしたい
    else:
        if S[cnt] == 'AND':
            # True-False
            # False-False
            # False-True
            count(cnt+1, False, ptn*2)
            count(cnt+1, True, ptn)
        else:
            # False-False
            count(cnt+1, False, ptn)
    return


if __name__ == '__main__':
    N = int(input())
    S = []
    ans = 0
    for _ in range(N):
        S.append(input())
    S.reverse()
    count(0, True, 1)

    print(ans)


