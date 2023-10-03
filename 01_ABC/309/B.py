

if __name__ == '__main__':
    N = int(input())
    A = []
    for _ in range(N):
        A.append(input())


    # １行目
    for i in range(N):
        if i == 0:
            print(A[1][0] + A[0][:-1])
        elif i == N-1:
            print(A[-1][1:] + A[-2][-1])
        else:
            print(A[i+1][0] + A[i][1:-1] + A[i-1][-1])

