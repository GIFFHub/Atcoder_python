import sys



def judge(prev_point, current_point):
    global history
    history[current_point-1] = True

    len_c = len(T[current_point-1])

    if len_c == 2:
        if T[current_point-1][0] == prev_point:
            next_point = T[current_point-1][1]
        else:
            next_point = T[current_point-1][0]

        # 既に経由した人だった場合
        if history[next_point-1]:
            return False
        # 新しい人だった場合
        else:
            # 次の人を判定しに行く
            return judge(current_point, next_point)
    else:
        return True


if __name__ == '__main__':

    sys.setrecursionlimit(100000)

    # input()
    N, M = map(int, input().split())
    A = []
    B = []
    T = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

        T[a-1].append(b)
        T[b-1].append(a)

    # 3人と隣接していたらダメ
    for t in T:
        if len(t) > 2:
            print('No')
            exit()

    # 全員両サイド隣接していたらダメ
    min_l = 2
    for t in T:
        min_l = min(min_l, len(t))
    if min_l == 2:
        print('No')
        exit()

    # 輪になったらダメ
    history = [False]*N
    for t_index, t_list in enumerate(T):
        for x in t_list:
            if not history[x-1]:
                if not judge(t_index+1, x):
                    print('No')
                    exit()
        history[t_index] = True
    print('Yes')




