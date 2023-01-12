from itertools import product


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(A[0])
    else:
        ans = 2**30+1
        for pro in product((0, 1), repeat=N-1):
            tmp = A[0]
            tmp_list = []
            for i, p in enumerate(pro):
                if p == 0:
                    tmp |= A[i+1]
                else:
                    tmp_list.append(tmp)
                    tmp = A[i+1]
            tmp_list.append(tmp)
            tmp_ans = tmp_list[0]
            for i in range(1, len(tmp_list)):
                tmp_ans ^= tmp_list[i]

            ans = min(ans, tmp_ans)

        print(ans)





