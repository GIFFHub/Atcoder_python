

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    min_A = min(A)
    max_A = max(A)
    sum_A = sum(A)

    tmp_result = sum_A - min_A - max_A

    for point in range(0, 101):
        if point <= min_A:
            result = tmp_result + min_A
        elif point >= max_A:
            result = tmp_result + max_A
        else:
            result = tmp_result + point

        if result >= X:
            print(point)
            break
    else:
        print(-1)


