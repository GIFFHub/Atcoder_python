if __name__ == '__main__':
    N = int(input())
    C1 = [0]
    C2 = [0]
    C1_tmp = 0
    C2_tmp = 0
    for _ in range(N):
        c, p = map(int, input().split())
        if c == 1:
            C1_tmp += p
        else:
            C2_tmp += p
        C1.append(C1_tmp)
        C2.append(C2_tmp)

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        C1_score = C1[r] - C1[l-1]
        C2_score = C2[r] - C2[l-1]
        print(C1_score, C2_score)

