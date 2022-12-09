s = set()
for _ in range(3):
    s.add(input()[1])
for i in 'BRGH':
    if i not in s:
        print('A'+i+'C')