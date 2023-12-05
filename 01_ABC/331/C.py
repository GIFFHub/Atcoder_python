import itertools
import bisect

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    sorted_A = sorted(A)

    crr_sorted_A = itertools.accumulate(sorted_A)

    Table = [0] + list(crr_sorted_A)
    ans = []
    for i in range(N):
        index = bisect.bisect_right(sorted_A, A[i])
        ans.append(sum_A - Table[index])

    print(*ans)






