import itertools

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    tmp_index = N-P.index(1)
    for i in range(1, N):
        #print(P[-i])

        # 後ろからn番目の値が後ろからn+1番目の値より小さいか
        # 小さい場合、次へ
        # 大きい場合、入れ替えて、ソートする
        if P[-i-1] < P[-i]:
            pass
        else:
            # -i-1番目と、次に小さい値を入れ替える
            for j in range(1, i+1):
                if P[-j] < P[-i-1]:
                    if P[-tmp_index] < P[-j]:
                        tmp_index = j
            P[-i-1], P[-tmp_index] = P[-tmp_index], P[-i-1]

            break
    tmp_list = P[-i:]
    tmp_list.sort(reverse=True)
    ans = P[:-i]+tmp_list
    print(*ans)



