def count(cnt, tobe):
    global ans
    if cnt == N:
        ans += 1
        return
    # 次をTrueにしたい
    if tobe:
        # 現状Trueパターン
        if S[cnt] == 'AND':
            # True-True
            count(cnt+1, True)
        else:
            # True-False
            # False-True
            count(cnt+1, True)
            count(cnt+1, False)
        # 現状Falseパターン
        if S[cnt] == 'AND':
            pass
        else:
            # True-False
            # False-True
            count(cnt+1, True)
    # 次をFalseにしたい
    else:
        # 現状Trueパターン
        if S[cnt] == 'AND':
            count(cnt+1, False)
        else:
            pass
        # 現状Falseパターン
        if S[cnt] == 'AND':
            count(cnt+1, True)
            count(cnt+1, False)
        else:
            count(cnt+1, False)
    return


if __name__ == '__main__':
    N = int(input())
    S = []
    ans = 0
    for _ in range(N):
        S.append(input())

    count(0, True)

    print(ans)


