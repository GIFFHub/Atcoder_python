from itertools import product

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    K = int(input())
    C = [0]*K
    D = [0]*K
    for i in range(K):
        c, d = map(int, input().split())
        C[i] = c
        D[i] = d
    ans = 0
    for pro in product((0, 1), repeat=K):
        balls = set()
        tmp_ans = 0
        for j, p in enumerate(pro):
            # Ciにボールをおく場合
            if p == 0:
                balls.add(C[j])
            else:
                balls.add(D[j])
        for k in range(M):
            if A[k] in balls and B[k] in balls:
                tmp_ans += 1
        ans = max(ans, tmp_ans)

    print(ans)



