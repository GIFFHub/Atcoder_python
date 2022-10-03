
if __name__ == '__main__':
    S = []
    for i in range(10):
        S.append(input())

    flg = 1
    first_point = [11, 11]
    final_point = [11, 11]
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if flg == 1:
                    first_point = [i, j]
                    flg = 0
                else:
                    final_point = [i, j]

    if final_point == [11, 11]:
        final_point = first_point

    A = first_point[0]+1
    B = final_point[0]+1
    C = first_point[1]+1
    D = final_point[1]+1

    print(A, B)
    print(C, D)






