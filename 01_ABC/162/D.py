import bisect


def check(A, B, C):
    global ans
    for first_index in range(0, len(A)):
        second_start_index = bisect.bisect(B, A[first_index])
        if second_start_index >= len(B):
            continue
        for second_index in range(second_start_index, len(B)):
            third_start_index = bisect.bisect(C, B[second_index])
            if third_start_index >= len(C):
                continue
            ans += len(C) - third_start_index
            target = B[second_index] + (B[second_index]-A[first_index])
            if C[0] <= target <= C[-1]:
                ans -= 1
            '''
            for third_index in range(third_start_index, len(C)):
                if (A[first_index]+C[third_index])//2 != B[second_index]:
                    ans += 1
            '''
    return


if __name__ == '__main__':
    N = int(input())
    S = input()
    R = []
    G = []
    B = []
    ans = 0
    for i, s in enumerate(S):
        if s == 'R':
            R.append(i)
        elif s == 'G':
            G.append(i)
        else:
            B.append(i)

    check(R, G, B)
    check(R, B, G)
    check(B, G, R)
    check(B, R, G)
    check(G, R, B)
    check(G, B, R)

    print(ans)
