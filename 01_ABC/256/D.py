

if __name__ == '__main__':
    N = int(input())
    T = []
    for _ in range(N):
        l, r = map(int, input().split())
        T.append((l,r))

    T.sort(key=lambda x: x[0])

    tmp_left = T[0][0]
    tmp_right = T[0][1]
    for i in range(N):
        if tmp_right >= T[i][0]:
            tmp_right = max(tmp_right, T[i][1])
        else:
            print(tmp_left, tmp_right)
            tmp_left = T[i][0]
            tmp_right = T[i][1]
    print(tmp_left, tmp_right)









