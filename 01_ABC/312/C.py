import bisect

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    set_A = set(A)
    set_B = set(B)
    set_AB = set_A.union(set_B)

    AB = list(set_AB)
    AB.sort()
    len_AB = len(AB)

    for i in range(len(AB)):
        A_num = bisect.bisect(A, AB[i])
        B_num = M - bisect.bisect_left(B, AB[i])

        if A_num >= B_num:
            print(AB[i])
            break

        A_num2 = bisect.bisect_left(A, AB[i]+1)
        B_num2 = M - bisect.bisect_left(B, AB[i]+1)

        if A_num2 >= B_num2:
            print(AB[i]+1)
            break


