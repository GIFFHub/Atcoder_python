import sys

sys.setrecursionlimit(50000000)

def shift(T):
    T = str(T)
    if len(T) == 1:
        return [int(T)]
    else:
        tmp = []
        tmp.append(int(T))
        for _ in range(len(T)-1):
            T = T[1:]+T[0]
            if T[0] != '0':
                tmp.append(int(T))
        return tmp


def check(table, cnt):
    global ans
    tmp = 0
    if ans >= cnt:
        for t in table:
            if t == 1:
                ans = min(ans, cnt+tmp)
            else:
                if t % a == 0:
                    t //= a
                    check(shift(t), cnt+tmp+1)
            tmp += 1


if __name__ == '__main__':
    s = set()
    a, N = map(int, input().split())
    ans = 10**6+1
    check(shift(N), 0)
    if ans == 10**6+1:
        print(-1)
    else:
        print(ans)





