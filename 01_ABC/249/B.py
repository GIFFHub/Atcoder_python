
S = input()
S_set = set(S)

if len(S) != len(S_set):
    print('No')

elif S.isupper() or S.islower():
    print('No')

else:
    print('Yes')