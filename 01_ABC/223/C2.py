

if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    time = 0
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        time += a/b

    end_time = time/2

    time = 0
    d = 0
    for i in range(N):
        time += A[i]/B[i]
        d += A[i]
        if time >= end_time:
            time -= A[i]/B[i]
            d -= A[i]
            remain_time = end_time-time
            d += remain_time * B[i]
            break

    print(d)

