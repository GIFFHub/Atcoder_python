
import math


def cal_vector(pos_i, pos_j):
    dx = pos_i[0]-pos_j[0]
    dy = pos_i[1]-pos_j[1]

    while True:
        tmp = math.gcd(dx, dy)
        if tmp != 1:
            dx //= tmp
            dy //= tmp
        else:
            break
    vec = (dx, dy)
    return vec


if __name__ == '__main__':
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    vecs = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            town_i = [X[i], Y[i]]
            town_j = [X[j], Y[j]]
            vecs.add(cal_vector(town_i, town_j))

    print(len(vecs))