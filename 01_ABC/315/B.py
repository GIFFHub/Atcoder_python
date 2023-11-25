if __name__ == '__main__':
    M = int(input())
    D = list(map(int, input().split()))
    sum_D = sum(D)
    half = sum_D // 2

    cnt = half
    month = 1
    day = 1
    while cnt > 0:
        day += 1
        if day > D[month-1]:
            day = 1
            month += 1
        cnt -= 1

    print(month, day)
