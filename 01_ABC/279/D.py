import math




def cal_time(g, a, b):
    return A/math.pow(g, (1/2)) + (g-1)*b


if __name__ == '__main__':
    A, B = map(int, input().split())

    g_kyoku = math.pow(A/(2*B), 2/3)

    g5 = math.floor(g_kyoku)
    g6 = math.ceil(g_kyoku)
    g4 = g5 - 1
    g3 = g4 - 1
    g2 = g3 - 1
    g1 = g2 - 1
    g0 = g1 - 1
    g7 = g6 + 1
    g8 = g7 + 1
    g9 = g8 + 1
    g10 = g9 + 1

    gs = [g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]

    ans = cal_time(1, A, B)

    for g_tmp in gs:
        if g_tmp >= 2:
            ans = min(ans, cal_time(g_tmp, A, B))

    print(ans)

