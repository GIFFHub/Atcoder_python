from collections import deque

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

    print(d)

    visit = [0] * (2*N+1)
    dq = deque()
    dq.append(1)

    for i in range(1, 2*N+1):
        if visit[i] == 1:
            continue
        else:
            visit[i] = 1
            while len(dq) > 0:
                current = dq.popleft()
                for nxt in d[current]:
                    if nxt == current:
                        pass
                    else:
                        if visit[nxt] == 1:
                            print('No')
                            exit()
                        else:
                            dq.append(nxt)
                            visit[nxt] = 1

    print('Yes')














