import numpy as np

def check2grid(a, b):
    x = a[0]-b[0]
    y = a[1]-b[1]

    x_check = (x == x[0])
    y_check = (y == y[0])

    if np.all(x_check) and np.all(y_check):
        return True
    else:
        return False




if __name__ == '__main__':
    N = int(input())
    S = np.empty((N, N))
    for i in range(N):
        s = input()
        for j in range(N):
            if s[j] == '.':
                S[i][j] = 0
            elif s[j] == '#':
                S[i][j] = 1

    T = np.empty((N, N))
    for i in range(N):
        t = input()
        for j in range(N):
            if t[j] == '.':
                T[i][j] = 0
            elif t[j] == '#':
                T[i][j] = 1

    if S.sum() != T.sum():
        print('No')

    elif S.sum() == 0:
        print('Yes')

    else:
        S2 = np.rot90(S)
        S3 = np.rot90(S2)
        S4 = np.rot90(S3)

        S_point = np.where(S == 1)
        S2_point = np.where(S2 == 1)
        S3_point = np.where(S3 == 1)
        S4_point = np.where(S4 == 1)
        T_point = np.where(T == 1)

        S_points = [S_point, S2_point, S3_point, S4_point]

        for sp in S_points:
            if check2grid(sp, T_point):
                print('Yes')
                break
        else:
            print('No')

