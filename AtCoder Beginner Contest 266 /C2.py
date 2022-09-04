import numpy as np
import math


def judge(P0, P1, P2, PX):

    p0x = P0[0]
    p0y = P0[1]
    p1x = P1[0]
    p1y = P1[1]
    p2x = P2[0]
    p2y = P2[1]
    px = PX[0]
    py = PX[1]

    area = 0.5 * (-p1y * p2x + p0y * (-p1x + p2x) + p0x * (p1y - p2y) + p1x * p2y)
    s = 1 / (2 * area) * (p0y * p2x - p0x * p2y + (p2y - p0y) * px + (p0x - p2x) * py)
    t = 1 / (2 * area) * (p0x * p1y - p0y * p1x + (p0y - p1y) * px + (p1x - p0x) * py)

    if (0 < s < 1) and (0 < t < 1) and (0 < 1-s-t < 1):
        return True
    else:
        return False


if __name__ == '__main__':

    A = np.array(list(map(int, input().split())), dtype=object)
    B = np.array(list(map(int, input().split())), dtype=object)
    C = np.array(list(map(int, input().split())), dtype=object)
    D = np.array(list(map(int, input().split())), dtype=object)

    if judge(A, B, C, D):
        print('No')
    elif judge(A, B, D, C):
        print('No')
    elif judge(A, C, D, B):
        print('No')
    elif judge(B, C, D, A):
        print('No')
    else:
        print('Yes')





