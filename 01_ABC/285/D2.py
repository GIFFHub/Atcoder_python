import sys
sys.setrecursionlimit(500000000)


def check(current_pos, prev_pos):
    global visit
    visit[current_pos] = 1
    for nxt in d[current_pos]:
        if nxt == prev_pos:
            pass
        else:
            if visit[nxt] == 1:
                return False
            else:
                check(nxt, current_pos)
    return True


if __name__ == '__main__':
    N = int(input())

    d = dict()
    d_alf = dict()
    tmp = 1
    for _ in range(N):
        s, t = input().split()
        d[tmp] = [tmp+1]
        d[tmp+1] = [tmp]

        if s not in d_alf:
            d_alf[s] = tmp
        else:
            d[tmp].append(d_alf[s])
            d[d_alf[s]].append(tmp)
        if t not in d_alf:
            d_alf[t] = tmp+1
        else:
            d[tmp+1].append(d_alf[t])
            d[d_alf[t]].append(tmp+1)

        tmp += 2

    visit = [0] * (2*N+1)
    for i in range(1, 2*N+1):
        if visit[i] == 0:
            if check(i, 0):
                continue
            else:
                print('No')
                break
    else:
        print('Yes')
















