import numpy as np

if __name__ == '__main__':
    # input
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    A = np.array(A)

    for a in A.T:
        print(*a)

