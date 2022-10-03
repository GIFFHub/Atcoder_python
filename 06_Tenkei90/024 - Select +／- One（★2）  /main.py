import numpy as np


if __name__ == '__main__':

    N, K = map(int, input().split())
    A = np.array(list(map(int, input().split())))
    B = np.array(list(map(int, input().split())))

    differ = np.sum(np.abs(A-B))

    if differ == K:
        print('Yes')
    elif differ < K:
        if (K - differ) % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')



