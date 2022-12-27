from math import factorial

if __name__ == '__main__':
    S = input()

    contains = 0
    not_contains = 0
    not_clear = 0

    for i in range(len(S)):
        if S[i] == 'o':
            contains += 1
        elif S[i] == 'x':
            not_contains += 1
        else:
            not_clear += 1
    ans = 0
    if contains == 4:
        ans += 4**4
    elif contains == 3:
        # containsのみ使う場合
        ans += 3**4
        # not_clearを1つ使う場合
        # どのnot_clearを使うか
        tmp = 4
        # どの
        ans += not_clear*contains*4*3*2*1

    elif contains == 2:
        # containsのみ使う場合
        ans += 2 ** 4
        # not_clearを1つ使う場合
        ans += not_clear*
    elif contains == 1:
        ans *= not_clear*(not_clear-1)*(not_clear-2)
    else:
        ans = not_clear*(not_clear-1)*(not_clear-2)*(not_clear-3)

    print(ans)


