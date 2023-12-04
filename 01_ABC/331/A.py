if __name__ == '__main__':
    M, D = map(int, input().split())
    y, m, d = map(int, input().split())

    ans_y = y
    ans_m = m
    ans_d = d
    if d < D:
        ans_d += 1
    else:
        if m < M:
            ans_m += 1
            ans_d = 1
        else:
            ans_y += 1
            ans_m = 1
            ans_d = 1

    print(ans_y, ans_m, ans_d)


