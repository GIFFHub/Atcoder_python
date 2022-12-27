
if __name__ == '__main__':
    S = input()

    contains = set()
    not_contains = set()
    not_clear = set()

    for i in range(len(S)):
        if S[i] == 'o':
            contains.add(i)
        elif S[i] == 'x':
            not_contains.add(i)
        else:
            not_clear.add(i)

    ans = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    tmp_contains = contains.copy()
                    if i in not_contains:
                        continue
                    if j in not_contains:
                        continue
                    if k in not_contains:
                        continue
                    if l in not_contains:
                        continue

                    if i in tmp_contains:
                        tmp_contains.remove(i)
                    if j in tmp_contains:
                        tmp_contains.remove(j)
                    if k in tmp_contains:
                        tmp_contains.remove(k)
                    if l in tmp_contains:
                        tmp_contains.remove(l)

                    if len(tmp_contains) == 0:
                        ans += 1
    print(ans)
