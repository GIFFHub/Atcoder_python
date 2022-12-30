from itertools import product

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        A[i] %= 200

    len_D = min(N, 8)
    D = A[:len_D]
    s = [-1]*200
    flg = 1
    for pro in product((0, 1), repeat=len_D):
        if flg:
            flg = 0
            continue
        else:
            tmp = 0
            for i, p in enumerate(pro):
                if p == 1:
                    tmp += D[i]
            tmp %= 200
            if s[tmp] != -1:
                B = s[tmp]
                C = pro
                break
            else:
                s[tmp] = pro
    else:
        print('No')
        exit()

    ans_b = [B.count(1)]
    ans_c = [C.count(1)]

    for i in range(len_D):
        if B[i] == 1:
            ans_b.append(i+1)
        if C[i] == 1:
            ans_c.append(i+1)

    print('Yes')
    print(*ans_b)
    print(*ans_c)













