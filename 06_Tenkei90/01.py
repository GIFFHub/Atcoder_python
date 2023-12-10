def binary_search(ok, ng):
    if ng - ok == 1:
        return ok
    mid = (ok + ng) // 2
    if check(mid):
        binary_search(mid, ng)
    else:
        binary_search(ok, mid)


def check(t):
    tmp = 0
    cnt = 0
    tmp_sum = 0
    for i in range(N):
        tmp_sum += A[i]
        tmp += A[i]
        if tmp >= t:
            tmp = 0
            cnt += 1
        if cnt >= K:
            if sum_A - tmp_sum >= t:
                return True
            else:
                return False
    return False


if __name__ == '__main__':
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)

    ans = binary_search(0, L)

    print(ans)
