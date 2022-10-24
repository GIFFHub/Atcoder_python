

if __name__ == '__main__':
    # input
    S = input()
    len_S = len(S)

    # 一文字の場合は既に回文
    if len_S == 1:
        print('Yes')
        exit()

    # Sの後ろに'a'がいくつ付いているか確認
    cnt_a_behind = 0
    cnt = 0
    while True:
        if len_S-1-cnt < 0:
            break
        if S[len_S-1-cnt] == 'a':
            cnt_a_behind += 1
        else:
            break
        cnt += 1

    # Sの前に'a'がいくつ付いているか確認
    cnt_a_top = 0
    cnt = 0
    while True:
        if cnt >= len_S:
            break
        if S[cnt] == 'a':
            cnt_a_top += 1
        else:
            break
        cnt += 1

    if cnt_a_top > cnt_a_behind:
        # 頭の'a'の方が多い場合、頭にいくら'a'をつけても回文にはならない
        print('No')
    else:
        # 頭の'a'と後ろの'a'を取り除いた文字列(S_check)が回文ならOK
        S_check = S[cnt_a_top:len_S-cnt_a_behind]
        len_S_check = len(S_check)
        for i in range(len_S_check//2):
            if S_check[i] == S_check[len_S_check-1-i]:
                continue
            else:
                print('No')
                break
        else:
            print('Yes')


