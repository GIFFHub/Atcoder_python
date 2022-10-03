
def cont(x, min_x, zero_x):
    max_x = max(x)
    max_x_index = A.index(max_x)

    mod_x = max_x % min_x
    A[max_x_index] = mod_x

    if mod_x == 0:
        zero_x += 1
    else:
        min_x = min(min_x, mod_x)

    return x, min_x, zero_x


def check_t(y, t):
    for i in range(len(y)):
        if y[i]//t != 0:
            return False # 奇数あり

    return True # 全部偶数


if __name__ == '__main__':

    N = int(input())
    A = list(map(int, input().split()))
    min_A = min(A)

    zero_A = 0
    cnt = 0

    while zero_A < N-1:
        cnt += 1

        if min_A == 1:
            tmp = len(A) - A.count(0) - 1
            zero_A += tmp
            cnt += tmp - 1
        elif min_A == 4 and check_t(min_A, A):
            tmp = len(A) - A.count(0) - 1
            zero_A += tmp
            cnt += tmp - 1

        else:
            A, min_A, zero_A = cont(A, min_A, zero_A)

    print(cnt)

