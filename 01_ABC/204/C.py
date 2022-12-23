import sys
sys.setrecursionlimit(5000000)


def dfs(current_pos):
    global city_num
    city_num += 1
    hist[current_pos-1] = True
    if current_pos in T:
        next_posses = T[current_pos]
        for next_pos in next_posses:
            # 行ったことなければ
            if not hist[next_pos-1]:
                dfs(next_pos)

    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    T = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        if a in T:
            T[a].append(b)
        else:
            T[a] = [b]

    ans = 0
    for i in range(1, N+1):
        hist = [False] * N
        city_num = 0
        dfs(i)
        ans += city_num

    print(ans)






