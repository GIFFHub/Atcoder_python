
def binary_search(ng, ok):
    if ok - ng == 1:
        return ok
    cen = (ok + ng) // 2
    if count_flyer(cen) < K:
        return binary_search(cen, ok)
    else:
        return binary_search(ng, cen)


def count_flyer(t):
    fly = 0
    for i in range(N):
        fly += t // A[i]
    return fly


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(binary_search(0, 10 ** 9 + 1))
