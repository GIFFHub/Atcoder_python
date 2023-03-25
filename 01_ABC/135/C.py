

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    S = sum(A)
    for i in range(N):
        if A[i] > B[i]:
            A[i] -= B[i]
        else:
            B[i] -= A[i]
            A[i] = 0
            A[i+1] = max(0, A[i+1] - B[i])

    print(S-sum(A))
