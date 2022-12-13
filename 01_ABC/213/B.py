

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A_sort = sorted(A)

    print(A.index(A_sort[-2])+1)

