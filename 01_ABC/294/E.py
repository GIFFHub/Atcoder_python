

if __name__ == '__main__':
    L, N1, N2 = map(int, input().split())
    V1 = []
    L1 = []
    V2 = []
    L2 = []
    for _ in range(N1):
        v, l = map(int, input().split())
        V1.append(v)
        L1.append(l)
    for _ in range(N2):
        v, l = map(int, input().split())
        V2.append(v)
        L2.append(l)

    L1_sum = L1[0]
    L2_sum = L2[0]
    t1 = 0
    t2 = 0
    prev_point = 0
    nxt_point = 0
    ans = 0
    S = sum(L1)
    while True:
        if L1_sum < L2_sum:
            nxt_point = L1_sum
            if V1[t1] == V2[t2]:
                ans += nxt_point - prev_point
            prev_point = nxt_point

            t1 += 1
            L1_sum += L1[t1]
        elif L1_sum > L2_sum:
            nxt_point = L2_sum
            if V1[t1] == V2[t2]:
                ans += nxt_point - prev_point
            prev_point = nxt_point
            t2 += 1
            L2_sum += L2[t2]
        else: # L1[t1] == L2[t2]
            nxt_point = L1_sum
            if V1[t1] == V2[t2]:
                ans += nxt_point - prev_point
            prev_point = nxt_point
            t1 += 1
            t2 += 1
            if t1 == N1 or t2 == N2:
                break
            L1_sum += L1[t1]
            L2_sum += L2[t2]
    print(ans)










