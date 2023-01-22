from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    S = input()
    T = input()
    d_s = defaultdict(int)
    d_t = defaultdict(int)

    for s in S:
        d_s[s] += 1
    for t in T:
        d_t[t] += 1

    ans = -1
    tmp_index = N
    if S == T:
        ans = 0
    elif d_t == d_s:
        for i in range(1, N+1):
            index = T[:tmp_index].rfind(S[-i])
            if index == -1:
                ans = N-(i-1)
                break
            else:
                tmp_index = index

    print(ans)

