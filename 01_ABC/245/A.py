A, B, C, D = map(int, input().split())
t = 'Takahashi'
a = 'Aoki'
if A > C:
    print(a)
elif A < C:
    print(t)
else:
    if B > D:
        print(a)
    elif B <= D:
        print(t)

