def cal(a, b):
    return 4*a*b + 3*a + 3*b


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))

    all_S = set()
    for a in range(1, 150):
        for b in range(a, 150):
            all_S.add(cal(a, b))


    ans = 0
    for s in S:
        if s in all_S:
            pass
        else:
            ans += 1

    print(ans)

