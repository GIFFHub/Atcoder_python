import bisect

if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A_rui = [sum(A)]
    tmp = A_rui[0]
    for a in A:
        tmp -= 2*a
        A_rui.append(tmp)

    for _ in range(Q):
        x = int(input())
        index = bisect.bisect_left(A, x)
        ans = A_rui[index] + x*index - x*(N-index)
        print(ans)





