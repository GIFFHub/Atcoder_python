def binary_search(ok, ng):
    if ng - ok == 1:
        return ok
    mid = (ok + ng) // 2
    if check(mid):
        return binary_search(mid, ng)
    else:
        return binary_search(ok, mid)


def check(t):
    tmp = 0
    cnt = 0
    tmp_sum = 0
    for i in range(N):
        tmp_sum += T[i]
        tmp += T[i]
        if tmp >= t:
            tmp = 0
            cnt += 1
        if cnt >= K:
            if L - tmp_sum >= t:
                return True
            else:
                return False
    return False


if __name__ == '__main__':
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    T = [A[0]]
    for i in range(1, N):
        T.append(A[i]-A[i-1])

    ans = binary_search(0, L)

    print(ans)
