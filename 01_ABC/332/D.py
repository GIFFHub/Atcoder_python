
import itertools


def check(h, w):
    for y in range(H):
        for x in range(W):
            if A[h[y]][w[x]] != B[y][x]:
                return False
    return True


def cal(T):
    len_T = len(T)
    base = list(range(len_T))
    T = list(T)
    cnt = 0
    for i in range(len_T):
        if base[i] != T[i]:
            cnt += T.index(i) - i
            T.remove(i)
            T.insert(i, i)
    return cnt


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = []
    B = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    for _ in range(H):
        B.append(list(map(int, input().split())))

    arr_h = list(itertools.permutations([x for x in range(H)]))
    arr_w = list(itertools.permutations([x for x in range(W)]))

    ans = 10000000000
    for h in arr_h:
        for w in arr_w:
            if check(h, w):
                ans = min(ans, cal(h)+cal(w))

    if ans == 10000000000:
        print(-1)
    else:
        print(ans)














