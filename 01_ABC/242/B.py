from collections import defaultdict
import string
d = defaultdict(int)

S = input()

for s in S:
    d[s] += 1
ans = ''
for i in string.ascii_letters:
    ans += i*d[i]

print(ans)




