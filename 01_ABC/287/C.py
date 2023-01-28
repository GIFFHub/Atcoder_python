import sys
sys.setrecursionlimit(50000000)


def visit(now, pre):
    if now not in d:
        print('No')
        exit()
    for nxt in d[now]:
        if nxt == pre:
            pass
        else:
            if not past[nxt]:
                past[nxt] = True
                visit(nxt, now)
            else:
                print('No')
                exit()


if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()

    for _ in range(M):
        u, v = map(int, input().split())
        if u in d:
            d[u].append(v)
        else:
            d[u] = [v]
        if v in d:
            d[v].append(u)
        else:
            d[v] = [u]

    start = 1
    past = [False]*(N+1)
    past[0] = True
    past[1] = True

    visit(1, 0)
    for p in past:
        if not p:
            print('No')
            break
    else:
        print('Yes')






