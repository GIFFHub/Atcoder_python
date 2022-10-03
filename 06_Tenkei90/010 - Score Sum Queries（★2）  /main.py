def calculate_cumulative(table):
    tmp = 0
    ans = []
    for j in range(len(table)):
        tmp += table[j][1]
        ans.append(tmp)
    return ans

def getstartindex(start, table):
    if table == []:
        return

    for i in range(len(table)):
        if table[i][2] > start:
            return i
        elif table[i][2] == start:
            return i
        elif table[i][2] < start:
            pass
    return None

def getendindex(end, table):
    if table == []:
        return
    if table[0][2] > end:
        return

    for i in range(len(table)):
        if table[i][2] == end:
            return i
        elif table[i][2] > end:
            return i-1
    return len(table)-1


if __name__ == '__main__':

    # input
    N = int(input())
    CP = []
    CP_1 = []
    CP_2 = []

    for _ in range(N):
        CP.append(list(map(int, input().split())))

    # CPの各行の３列目に出席番号追加
    for i in range(N):
        CP[i].append(i+1)

    for i in range(N):
        if CP[i][0] == 1:
            CP_1.append(CP[i])
        else:
            CP_2.append(CP[i])

    Q = int(input())
    LP = []
    for _ in range(Q):
        LP.append(list(map(int, input().split())))

    # 累積和配列を求める
    CP_1_curu = calculate_cumulative(CP_1)
    CP_2_curu = calculate_cumulative(CP_2)

    for i in range(Q):
        start = LP[i][0]
        end = LP[i][1]

        CP_2_start_index = getstartindex(start, CP_2)
        if CP_2_start_index == 0 or CP_2_start_index is None:
            CP_2_start = 0
        else:
            CP_2_start = CP_2_curu[CP_2_start_index-1]

        CP_2_end_index = getendindex(end, CP_2)
        if CP_2_end_index is None:
            CP_2_end = 0
        else:
            CP_2_end = CP_2_curu[CP_2_end_index]
        sum_2 = CP_2_end - CP_2_start

        CP_1_start_index = getstartindex(start, CP_1)
        if CP_1_start_index == 0 or CP_1_start_index is None:
            CP_1_start = 0
        else:
            CP_1_start = CP_1_curu[CP_1_start_index-1]

        CP_1_end_index = getendindex(end, CP_1)
        if CP_1_end_index is None:
            CP_1_end = 0
        else:
            CP_1_end = CP_1_curu[CP_1_end_index]

        sum_1 = CP_1_end - CP_1_start

        print(sum_1, sum_2)




