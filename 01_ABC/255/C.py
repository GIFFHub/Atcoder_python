

if __name__ == '__main__':
    R, C = map(int, input().split())
    a11, a12 = map(int, input().split())
    a21, a22 = map(int, input().split())

    A = [[a11, a12], [a21, a22]]

    print(A[R-1][C-1])