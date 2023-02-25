

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1]*(4*M) >= sum(A):
        print('Yes')
    else:
        print('No')