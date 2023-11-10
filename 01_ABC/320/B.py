def check(Str):
    len_Str = len(Str)
    for i in range(len_Str//2):
        if Str[i] != Str[-i-1]:
            return False
    return True


if __name__ == '__main__':
    S = input()
    len_S = len(S)
    tmp_len = len_S
    flg = 0
    while tmp_len >= 1:
        for i in range(len_S - tmp_len+1):
            start_index = i
            end_index = start_index + tmp_len
            if check(S[start_index:end_index]):
                ans = tmp_len
                flg = 1
                break
        tmp_len -= 1
        if flg:
            break
    print(ans)



