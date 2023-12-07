if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    shift = 0
    for _ in range(Q):
        t, x, y = map(int, input().split())
        x_shift = (x+shift-1) % N
        y_shift = (y+shift-1) % N
        if t == 1:
            A[x_shift], A[y_shift] = A[y_shift], A[x_shift]
        elif t == 2:
            shift -= 1
        else:
            print(A[x_shift])
