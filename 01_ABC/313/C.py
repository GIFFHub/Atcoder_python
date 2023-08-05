

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    # 最終形は決まってる
    # 最終形は必ず２種類の数値で構成される

    sum_A = sum(A)
    min_num = sum_A // N
    rest = N - sum_A % N

    B = [0]*N
    for i in range(N):
        if rest > 0:
            B[i] = min_num
            rest -= 1
        else:
            B[i] = min_num + 1

    ans = 0
    for j in range(N):
        if A[j] <= B[j]:
            ans += B[j] - A[j]
        else:
            break

    print(ans)
