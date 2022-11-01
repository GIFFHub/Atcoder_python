
def binary_search(target, ng, ok, table):
    if ok-ng == 1:
        return ok
    cen = (ok+ng)//2
    if table[cen] > target:
        return binary_search(target, cen, ok, table)
    else:
        return binary_search(target, ng, cen, table)


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P_K = P[:K]
    P_K.sort(reverse=True)
    print(P_K[K-1])

    for i in range(K, N):
        index = binary_search(P[i], -1, len(P_K), P_K)
        P_K = P_K[:index]+[P[i]]+P_K[index:]
        print(P_K[K-1])








