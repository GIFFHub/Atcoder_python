
def cal_cost(prev_pos, current_pos):

    cost = DP[prev_pos]+abs(H[current_pos]-H[prev_pos])
    return cost


def cal_min_cost(current_pos):
    tmp_cost = 10**4+1
    min_cost = tmp_cost
    for n in range(1, K+1):
        if current_pos >= n:
            min_cost = min(min_cost, cal_cost(current_pos-n, current_pos))

    return min_cost


if __name__ == '__main__':
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    DP = [0 for _ in range(N)]

    for i in range(1, N):
        DP[i] = cal_min_cost(i)

    print(DP[N-1])

