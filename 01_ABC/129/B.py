

if __name__ == '__main__':
    N = int(input())
    Q = list(map(int, input().split()))
    sum_Q = sum(Q)

    S1 = 0
    S2 = sum_Q
    ans = sum_Q
    for q in Q:
        S1 += q
        S2 -= q
        ans = min(ans, abs(S1-S2))

    print(ans)