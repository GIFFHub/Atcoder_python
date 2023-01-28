import sys
import itertools

if __name__ == '__main__':
    X = list(input())
    X = list(map(int, X))

    acc = list(itertools.accumulate(X))
    acc.reverse()

    nxt = 0
    ans = []
    for x in acc:
        cur = x + nxt
        nxt, cur = divmod(cur, 10)
        ans.append(str(cur))

    ans.reverse()

    if nxt == 0:
        nxt = ''
    else:
        nxt = str(nxt)
    ans = nxt + ''.join(ans)
    print(ans)


