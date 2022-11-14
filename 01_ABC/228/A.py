

S, T, X = map(int, input().split())


if S <= T:
    if S <= X <= T:
        print('Yes')
    else:
        print('No')
else:
    if not T < X < S:
        print('Yes')
    else:
        print('No')