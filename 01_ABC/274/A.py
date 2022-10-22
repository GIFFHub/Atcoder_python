A, B = map(int, input().split())

S_int = B/A
S_str = str(S_int)
S_str += '0000000'
if int(S_str[5]) > 4:
    S_int += 0.001
S_str = str(S_int)
S_str += '0000000'

print(S_str[:5])