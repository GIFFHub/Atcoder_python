
if __name__ == '__main__':

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum([A[x] for x in range(M)])

    print(sum_A)



