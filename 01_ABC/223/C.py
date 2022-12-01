if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    time_front = []
    time_back = []
    tmp_front = 0
    tmp_back = 0
    for i in range(N):
        tmp_front += A[i] / B[i]
        tmp_back += A[- i - 1] / B[- i - 1]
        time_front.append(tmp_front)
        time_back.append(tmp_back)

    tmp_front = 0
    tmp_back = 0
    d_front = 0
    d_back = 0
    cnt_front = 0
    cnt_back = 0
    end_time = time_front[-1]
    flg = True  # 最後に燃やした方フラグ

    while True:
        if tmp_front + time_front[cnt_front] <= tmp_back + time_back[cnt_back]:
            tmp_front += A[cnt_front]/B[cnt_back]
            cnt_front += 1
            d_front += A[cnt_front]
            flg = True
        else:
            tmp_back += A[cnt_back]/B[cnt_back]
            cnt_back += 1
            d_back += A[cnt_back]
            flg = False

        if tmp_front + tmp_back >= end_time:
            break

    if tmp_front + tmp_back == end_time:
        print(tmp_front)
    else:
        if flg:
            cnt_front -= 1
            tmp_front -= A[cnt_front]/B[cnt_front]
            d_front -= A[cnt_front]
        else:
            cnt_back -= 1
            tmp_back -= A[cnt_back]/B[cnt_back]
            d_back -= A[cnt_back]

        ans = d_front + (A[cnt_front] + B[cnt_front]*(tmp_front-tmp_back)) / 2
        print(ans)
