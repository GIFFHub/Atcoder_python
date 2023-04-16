S = input()
r = S.count('0')
b = len(S) - r

print(2 * min(r, b))