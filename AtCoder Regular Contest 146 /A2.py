import itertools

if __name__ == '__main__':

    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    ans = 0


    arr = list(itertools.permutations([x for x in range(3)]))
    for x in arr:
        ans = max(ans, int(str(A[x[0]])+str(A[x[1]])+str(A[x[2]])))

    print(ans)

